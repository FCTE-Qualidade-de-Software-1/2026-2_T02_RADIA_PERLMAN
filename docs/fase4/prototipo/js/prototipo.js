(function () {
  "use strict";

  var DADOS = window.INDICADORES_DADOS;
  var SVG_NS = "http://www.w3.org/2000/svg";

  var MESES_LONGOS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"];
  var MESES_CURTOS = ["jan", "fev", "mar", "abr", "mai", "jun",
    "jul", "ago", "set", "out", "nov", "dez"];

  function pad2(n) { return (n < 10 ? "0" : "") + n; }
  function horasMinutos(h) {
    var total = Math.round(h * 60);
    return { h: Math.floor(total / 60), m: total % 60 };
  }
  function fmtHoras(h) {
    var t = horasMinutos(h);
    return t.h + " h " + pad2(t.m) + " min";
  }
  function falarHoras(h) {
    var t = horasMinutos(h);
    if (t.h === 0 && t.m === 0) return "0 horas";
    var partes = [];
    if (t.h > 0) partes.push(t.h + (t.h === 1 ? " hora" : " horas"));
    if (t.m > 0) partes.push(t.m + (t.m === 1 ? " minuto" : " minutos"));
    return partes.join(" e ");
  }
  function fmtNumero(n) { return String(n).replace(".", ","); }
  function fmtVezes(n) { return n + (n === 1 ? " vez" : " vezes"); }
  function fmtLimiteHoras(v) { return fmtNumero(v) + " h"; }

  var INDICADORES = {
    dic: {
      nome: "Tempo sem energia", sigla: "DIC",
      tituloGrafico: "Tempo sem energia por mês",
      fmt: fmtHoras, falar: falarHoras, fmtLimite: fmtLimiteHoras, falarLimite: falarHoras,
      fmtEixo: fmtLimiteHoras, inteiro: false
    },
    fic: {
      nome: "Vezes sem energia", sigla: "FIC",
      tituloGrafico: "Vezes sem energia por mês",
      fmt: fmtVezes, falar: fmtVezes, fmtLimite: fmtVezes, falarLimite: fmtVezes,
      fmtEixo: function (v) { return String(v); }, inteiro: true
    },
    dmic: {
      nome: "Maior falta seguida", sigla: "DMIC",
      tituloGrafico: "Maior falta seguida por mês",
      fmt: fmtHoras, falar: falarHoras, fmtLimite: fmtLimiteHoras, falarLimite: falarHoras,
      fmtEixo: fmtLimiteHoras, inteiro: false
    }
  };
  var ORDEM = ["dic", "fic", "dmic"];

  function partesMes(chave) {
    var p = chave.split("-");
    return { ano: Number(p[0]), mes: Number(p[1]) };
  }
  function rotuloMes(chave) { var p = partesMes(chave); return MESES_LONGOS[p.mes - 1] + "/" + p.ano; }
  function falarMes(chave) { var p = partesMes(chave); return MESES_LONGOS[p.mes - 1] + " de " + p.ano; }
  function curtoMes(chave) { return MESES_CURTOS[partesMes(chave).mes - 1]; }
  function maiuscula(t) { return t.charAt(0).toUpperCase() + t.slice(1); }

  function acima(reg, ind) { return reg.apurado[ind] > reg.limite[ind]; }
  function mesAcima(reg) { return ORDEM.some(function (i) { return acima(reg, i); }); }

  var params = new URLSearchParams(window.location.search);
  var cenarioInicial = params.get("cenario");
  if (["real", "ficticio", "carregando", "erro"].indexOf(cenarioInicial) === -1) cenarioInicial = "real";

  var estado = {
    cenario: cenarioInicial,
    de: null,
    ate: null,
    indicador: "dic",
    mesSel: null,
    verTabela: false
  };

  function registros() {
    var c = DADOS.cenarios[estado.cenario];
    return c ? c.registros : DADOS.cenarios.real.registros;
  }

  function registrosPeriodo() {
    var todos = registros();
    var i = todos.findIndex(function (r) { return r.mes === estado.de; });
    var f = todos.findIndex(function (r) { return r.mes === estado.ate; });
    if (i < 0) i = 0;
    if (f < 0) f = todos.length - 1;
    return todos.slice(Math.min(i, f), Math.max(i, f) + 1);
  }

  function registroSelecionado(regs) {
    var r = regs.find(function (x) { return x.mes === estado.mesSel; });
    if (!r) { r = regs[regs.length - 1]; estado.mesSel = r.mes; }
    return r;
  }

  function $(id) { return document.getElementById(id); }
  function el(tag, classe, texto) {
    var e = document.createElement(tag);
    if (classe) e.className = classe;
    if (texto != null) e.textContent = texto;
    return e;
  }
  function svg(tag, attrs) {
    var e = document.createElementNS(SVG_NS, tag);
    if (attrs) Object.keys(attrs).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    return e;
  }

  var temporizadorAviso = null;
  function avisar(texto) {
    var a = $("aviso-flutuante");
    a.textContent = texto;
    a.hidden = false;
    clearTimeout(temporizadorAviso);
    temporizadorAviso = setTimeout(function () { a.hidden = true; }, 3000);
  }

  function configurarSeletor(grupo, atributo, aoEscolher) {
    var botoes = Array.prototype.slice.call(grupo.querySelectorAll("button"));
    botoes.forEach(function (b, i) {
      b.addEventListener("click", function () { aoEscolher(b.getAttribute(atributo)); });
      b.addEventListener("keydown", function (ev) {
        var alvo = null;
        if (ev.key === "ArrowRight" || ev.key === "ArrowDown") alvo = botoes[(i + 1) % botoes.length];
        if (ev.key === "ArrowLeft" || ev.key === "ArrowUp") alvo = botoes[(i - 1 + botoes.length) % botoes.length];
        if (ev.key === "Home") alvo = botoes[0];
        if (ev.key === "End") alvo = botoes[botoes.length - 1];
        if (alvo) { ev.preventDefault(); aoEscolher(alvo.getAttribute(atributo)); alvo.focus(); }
      });
    });
  }
  function atualizarSeletor(grupo, atributo, valor) {
    grupo.querySelectorAll("button").forEach(function (b) {
      var ativo = b.getAttribute(atributo) === valor;
      b.setAttribute("aria-checked", ativo ? "true" : "false");
      b.tabIndex = ativo ? 0 : -1;
    });
  }

  function passoBonito(bruto) {
    var exp = Math.pow(10, Math.floor(Math.log10(bruto)));
    var f = bruto / exp;
    return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * exp;
  }

  function caminhoBarra(x, y, w, h) {
    var r = Math.min(4, h, w / 2);
    return "M" + x + "," + (y + h) + "V" + (y + r) +
      "Q" + x + "," + y + " " + (x + r) + "," + y + "H" + (x + w - r) +
      "Q" + (x + w) + "," + y + " " + (x + w) + "," + (y + r) + "V" + (y + h) + "Z";
  }

  function descricaoColuna(reg, chave) {
    var ind = INDICADORES[chave];
    return falarMes(reg.mes) + ": " + ind.falar(reg.apurado[chave]) +
      ", limite " + ind.falarLimite(reg.limite[chave]) +
      (acima(reg, chave) ? ", acima do limite" : "");
  }

  function mostrarDica(reg, cx, topoY) {
    var chave = estado.indicador;
    var ind = INDICADORES[chave];
    var dica = $("dica");
    dica.innerHTML = "";
    dica.appendChild(el("strong", null, ind.fmt(reg.apurado[chave])));
    dica.appendChild(el("span", null, rotuloMes(reg.mes) + " · limite " + ind.fmtLimite(reg.limite[chave])));
    if (acima(reg, chave)) dica.appendChild(el("span", "dica__acima", "Acima do limite"));
    dica.hidden = false;
    var area = $("grafico-area");
    var x = Math.max(4, Math.min(cx - dica.offsetWidth / 2, area.clientWidth - dica.offsetWidth - 4));
    dica.style.left = x + "px";
    dica.style.top = Math.max(0, topoY - dica.offsetHeight - 10) + "px";
  }
  function esconderDica() { $("dica").hidden = true; }

  function renderGrafico(regs, manterFoco) {
    var chave = estado.indicador;
    var ind = INDICADORES[chave];
    var area = $("grafico-area");
    var alvo = $("grafico-svg");

    $("grafico-titulo").textContent = estado.verTabela ? "Indicadores por mês" : ind.tituloGrafico;

    var largura = Math.max(280, Math.round(area.clientWidth || 600));
    var estreito = largura < 520;
    var altura = estreito ? 220 : 260;
    var m = { topo: 22, dir: 8, base: 42, esq: estreito ? 38 : 46 };
    var pw = largura - m.esq - m.dir;
    var ph = altura - m.topo - m.base;

    var valores = regs.map(function (r) { return r.apurado[chave]; });
    var lim = regs[regs.length - 1].limite[chave];
    var topo = Math.max(lim * 1.3, Math.max.apply(null, valores) * 1.15, ind.inteiro ? 4 : 1);
    var passo = passoBonito(topo / 4);
    if (ind.inteiro) passo = Math.max(1, Math.round(passo));
    var yMax = Math.ceil(topo / passo) * passo;
    function y(v) { return m.topo + ph - (v / yMax) * ph; }

    var banda = pw / regs.length;
    var larguraBarra = Math.min(24, banda * 0.55);

    var n = regs.length;
    var mostrarRotulo = regs.map(function (r, i) { return banda >= 30 || (n - 1 - i) % 2 === 0; });
    var iSel = regs.findIndex(function (r) { return r.mes === estado.mesSel; });
    if (iSel >= 0 && !mostrarRotulo[iSel]) {
      mostrarRotulo[iSel] = true;
      if (iSel > 0) mostrarRotulo[iSel - 1] = false;
      if (iSel < n - 1) mostrarRotulo[iSel + 1] = false;
    }

    var raiz = svg("svg", {
      viewBox: "0 0 " + largura + " " + altura, width: largura, height: altura,
      role: "radiogroup", "aria-labelledby": "grafico-titulo", "aria-describedby": "grafico-instrucao"
    });

    var grade = svg("g", { "aria-hidden": "true" });
    for (var t = 0; t <= yMax + 1e-9; t += passo) {
      var yy = Math.round(y(t)) + 0.5;
      grade.appendChild(svg("line", { x1: m.esq, x2: m.esq + pw, y1: yy, y2: yy, "class": t === 0 ? "base" : "grade" }));
      var rot = svg("text", { x: m.esq - 8, y: yy + 4, "text-anchor": "end", "class": "eixo-texto" });
      rot.textContent = ind.fmtEixo(Math.round(t * 100) / 100);
      grade.appendChild(rot);
    }
    raiz.appendChild(grade);

    var colunas = [];
    var anoAnterior = null;
    regs.forEach(function (reg, i) {
      var v = reg.apurado[chave];
      var ehAcima = acima(reg, chave);
      var selecionado = reg.mes === estado.mesSel;
      var x0 = m.esq + i * banda;
      var cx = x0 + banda / 2;

      var g = svg("g", {
        "class": "coluna", role: "radio",
        "aria-checked": selecionado ? "true" : "false",
        "aria-label": descricaoColuna(reg, chave),
        tabindex: selecionado ? "0" : "-1"
      });
      g.appendChild(svg("rect", { "class": "coluna__fundo", x: x0 + 1, y: m.topo - 16, width: banda - 2, height: ph + 16 + 22, rx: 4 }));
      g.appendChild(svg("rect", { "class": "coluna__foco", x: x0 + 2, y: m.topo - 15, width: banda - 4, height: ph + 15 + 21, rx: 4 }));

      var yTopo = y(0);
      if (v > 0) {
        var h = Math.max(2, y(0) - y(v));
        yTopo = y(0) - h;
        g.appendChild(svg("path", { "class": "barra" + (ehAcima ? " barra--acima" : ""), d: caminhoBarra(cx - larguraBarra / 2, yTopo, larguraBarra, h) }));
      }
      if (mostrarRotulo[i]) {
        var tx = svg("text", { x: cx, y: m.topo + ph + 17, "text-anchor": "middle", "class": "eixo-texto" });
        tx.textContent = curtoMes(reg.mes);
        g.appendChild(tx);
      }
      raiz.appendChild(g);
      colunas.push({ g: g, reg: reg, cx: cx, topo: yTopo });

      var ano = partesMes(reg.mes).ano;
      if (ano !== anoAnterior) {
        var ta = svg("text", { x: x0 + 4, y: m.topo + ph + 35, "class": "eixo-ano", "aria-hidden": "true" });
        ta.textContent = String(ano);
        raiz.appendChild(ta);
        if (anoAnterior !== null) {
          raiz.appendChild(svg("line", { x1: x0, x2: x0, y1: m.topo + ph, y2: m.topo + ph + 38, "class": "grade", "aria-hidden": "true" }));
        }
        anoAnterior = ano;
      }
    });

    var yl = Math.round(y(lim)) + 0.5;
    var gLim = svg("g", { "aria-hidden": "true", "pointer-events": "none" });
    gLim.appendChild(svg("line", { x1: m.esq, x2: m.esq + pw, y1: yl, y2: yl, "class": "linha-limite" }));
    var rl = svg("text", { x: m.esq + pw, y: yl - 5, "text-anchor": "end", "class": "rotulo-limite" });
    rl.textContent = "limite " + ind.fmtLimite(lim);
    gLim.appendChild(rl);
    raiz.appendChild(gLim);

    var focoNoGrafico = manterFoco || (document.activeElement && alvo.contains(document.activeElement));
    alvo.innerHTML = "";
    alvo.appendChild(raiz);

    colunas.forEach(function (c, i) {
      c.g.addEventListener("click", function () { selecionarMes(c.reg.mes, true); });
      c.g.addEventListener("pointerenter", function () { mostrarDica(c.reg, c.cx, c.topo); });
      c.g.addEventListener("pointerleave", function () { if (!c.g.classList.contains("tem-foco")) esconderDica(); });
      c.g.addEventListener("focus", function () { c.g.classList.add("tem-foco"); mostrarDica(c.reg, c.cx, c.topo); });
      c.g.addEventListener("blur", function () { c.g.classList.remove("tem-foco"); esconderDica(); });
      c.g.addEventListener("keydown", function (ev) {
        var d = null;
        if (ev.key === "ArrowRight" || ev.key === "ArrowDown") d = Math.min(colunas.length - 1, i + 1);
        if (ev.key === "ArrowLeft" || ev.key === "ArrowUp") d = Math.max(0, i - 1);
        if (ev.key === "Home") d = 0;
        if (ev.key === "End") d = colunas.length - 1;
        if (d !== null) { ev.preventDefault(); selecionarMes(colunas[d].reg.mes, true); }
      });
    });

    if (focoNoGrafico) {
      var sel = alvo.querySelector('.coluna[aria-checked="true"]');
      if (sel) sel.focus();
    }

    $("grafico-vazio").hidden = !valores.every(function (v) { return v === 0; });
    $("legenda-acima").hidden = !regs.some(function (r) { return acima(r, chave); });
  }

  function renderTabela(regs) {
    $("tabela-legenda").textContent = "Indicadores de continuidade de " + rotuloMes(regs[0].mes) +
      " a " + rotuloMes(regs[regs.length - 1].mes) + ". Limites por mês: " +
      ORDEM.map(function (c) { return INDICADORES[c].nome.toLowerCase() + " " + INDICADORES[c].fmtLimite(regs[0].limite[c]); }).join(", ") + ".";
    ORDEM.forEach(function (c) {
      var th = $("th-" + c);
      th.textContent = c === "dic" ? "Tempo sem energia" : c === "fic" ? "Vezes" : "Maior falta";
      th.appendChild(el("span", "tabela__limite", "limite " + INDICADORES[c].fmtLimite(regs[regs.length - 1].limite[c])));
    });
    var corpo = $("tabela-corpo");
    corpo.innerHTML = "";
    regs.forEach(function (reg) {
      var tr = el("tr");
      var th = el("th", null, rotuloMes(reg.mes));
      th.scope = "row";
      tr.appendChild(th);
      ORDEM.forEach(function (chave) {
        var ehAcima = acima(reg, chave);
        var td = el("td", null, INDICADORES[chave].fmt(reg.apurado[chave]));
        if (ehAcima) td.appendChild(el("span", "sr-only", ", acima do limite"));
        tr.appendChild(td);
      });
      corpo.appendChild(tr);
    });
  }

  function renderDetalhe(reg) {
    $("detalhe-titulo").textContent = maiuscula(rotuloMes(reg.mes));
    var lista = $("detalhe-corpo");
    lista.innerHTML = "";
    ORDEM.forEach(function (chave) {
      var ind = INDICADORES[chave];
      var ehAcima = acima(reg, chave);
      var li = el("li", "mes__item" + (ehAcima ? " mes__item--acima" : ""));
      var nome = el("p", "mes__nome", ind.nome + " ");
      var sigla = el("abbr", null, "(" + ind.sigla + ")");
      sigla.style.textDecoration = "none";
      nome.appendChild(sigla);
      li.appendChild(nome);
      var valor = el("p", "mes__valor");
      valor.appendChild(document.createTextNode(ind.fmt(reg.apurado[chave])));
      if (ehAcima) valor.appendChild(el("span", "sr-only", ", acima do limite"));
      li.appendChild(valor);
      li.appendChild(el("p", "mes__limite", "limite " + ind.fmtLimite(reg.limite[chave])));
      lista.appendChild(li);
    });
  }

  function render() {
    var carregando = estado.cenario === "carregando";
    var erro = estado.cenario === "erro";
    $("estado-carregando").hidden = !carregando;
    $("estado-erro").hidden = !erro;
    $("conteudo-indicadores").hidden = carregando || erro;
    document.querySelector(".filtros").hidden = carregando || erro;

    var c = DADOS.cenarios[estado.cenario];
    // Com painel=0 (sessões com participantes), o cenário não é descrito, para não entregar respostas
    $("proto-rotulo-cenario").textContent = params.get("painel") === "0" ? "" :
      (c ? c.rotulo : (carregando ? "Estado: carregando" : "Estado: dados indisponíveis"));
    $("proto-cenario").value = estado.cenario;

    atualizarSeletor($("indicador"), "data-indicador", estado.indicador);

    if (carregando || erro) return;

    var regs = registrosPeriodo();
    var sel = registroSelecionado(regs);
    renderGrafico(regs);
    renderTabela(regs);
    renderDetalhe(sel);
  }

  function selecionarMes(mes, focarGrafico) {
    estado.mesSel = mes;
    var regs = registrosPeriodo();
    renderGrafico(regs, focarGrafico);
    renderTabela(regs);
    renderDetalhe(registroSelecionado(regs));
  }

  function preencherSelectsPeriodo() {
    var todos = registros();
    ["periodo-de", "periodo-ate"].forEach(function (id) {
      var s = $(id);
      s.innerHTML = "";
      todos.forEach(function (r) {
        var o = el("option", null, rotuloMes(r.mes));
        o.value = r.mes;
        s.appendChild(o);
      });
    });
    if (!estado.de) estado.de = todos[0].mes;
    if (!estado.ate) estado.ate = todos[todos.length - 1].mes;
    $("periodo-de").value = estado.de;
    $("periodo-ate").value = estado.ate;
  }

  function baixarCsv() {
    var regs = registrosPeriodo();
    var linhas = [["Mês", "Tempo sem energia (h)", "Limite tempo (h)", "Vezes sem energia", "Limite vezes",
      "Maior falta seguida (h)", "Limite maior falta (h)", "Situação"]];
    regs.forEach(function (r) {
      linhas.push([rotuloMes(r.mes),
        fmtNumero(r.apurado.dic), fmtNumero(r.limite.dic),
        String(r.apurado.fic), String(r.limite.fic),
        fmtNumero(r.apurado.dmic), fmtNumero(r.limite.dmic),
        mesAcima(r) ? "Acima do limite" : "Dentro do limite"]);
    });
    var csv = "﻿" + linhas.map(function (l) {
      return l.map(function (c) { return '"' + String(c).replace(/"/g, '""') + '"'; }).join(";");
    }).join("\r\n");
    var url = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
    var a = el("a");
    a.href = url;
    a.download = "indicadores-continuidade_" + regs[0].mes + "_a_" + regs[regs.length - 1].mes + ".csv";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    avisar("Planilha baixada.");
  }

  var ajudaAbertaAntes = false;
  window.addEventListener("beforeprint", function () { var d = document.querySelector(".ajuda"); ajudaAbertaAntes = d.open; d.open = true; });
  window.addEventListener("afterprint", function () { document.querySelector(".ajuda").open = ajudaAbertaAntes; });

  function iniciar() {
    $("uc-codigo").textContent = DADOS.uc.codigoCliente;
    $("uc-cpf").textContent = DADOS.uc.cpf;
    $("uc-endereco").textContent = DADOS.uc.endereco;
    $("uc-numero").textContent = DADOS.uc.unidadeConsumidora;
    $("uc-situacao").textContent = DADOS.uc.situacao;

    if (params.get("painel") === "0") $("proto-controle").hidden = true;

    preencherSelectsPeriodo();
    configurarSeletor($("indicador"), "data-indicador", function (v) { estado.indicador = v; render(); });

    $("periodo-de").addEventListener("change", function () {
      estado.de = this.value;
      if (estado.de > estado.ate) { estado.ate = estado.de; $("periodo-ate").value = estado.ate; }
      render();
    });
    $("periodo-ate").addEventListener("change", function () {
      estado.ate = this.value;
      if (estado.ate < estado.de) { estado.de = estado.ate; $("periodo-de").value = estado.de; }
      render();
    });

    $("proto-cenario").addEventListener("change", function () {
      estado.cenario = this.value;
      var u = new URL(window.location.href);
      u.searchParams.set("cenario", estado.cenario);
      window.history.replaceState(null, "", u);
      render();
    });

    $("tentar-novamente").addEventListener("click", function () {
      estado.cenario = "carregando";
      render();
      setTimeout(function () { estado.cenario = "real"; render(); $("grafico-titulo").focus(); }, 900);
    });

    $("alternar-tabela").addEventListener("click", function () {
      estado.verTabela = !estado.verTabela;
      $("tabela-container").hidden = !estado.verTabela;
      $("grafico-area").hidden = estado.verTabela;
      $("indicador-grupo").hidden = estado.verTabela;
      $("grafico-instrucao").hidden = estado.verTabela;
      $("detalhe").hidden = estado.verTabela;
      this.setAttribute("aria-expanded", estado.verTabela ? "true" : "false");
      this.textContent = estado.verTabela ? "Ver gráfico" : "Ver tabela";
      renderGrafico(registrosPeriodo());
    });

    $("baixar-csv").addEventListener("click", baixarCsv);
    $("salvar-pdf").addEventListener("click", function () { window.print(); });

    document.querySelectorAll("[data-proto-link]").forEach(function (a) {
      a.addEventListener("click", function (ev) { ev.preventDefault(); avisar("No protótipo, este link não leva a outra página."); });
    });

    var pendente = false;
    if ("ResizeObserver" in window) {
      new ResizeObserver(function () {
        if (pendente || estado.verTabela || !DADOS.cenarios[estado.cenario]) return;
        pendente = true;
        requestAnimationFrame(function () { pendente = false; renderGrafico(registrosPeriodo()); });
      }).observe($("grafico-area"));
    }

    render();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();

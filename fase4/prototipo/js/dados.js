(function () {
  "use strict";

  var LIMITES = { dic: 7, fic: 3, dmic: 5 };

  var MESES = [
    "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03",
    "2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"
  ];

  function serie(valores) {
    return MESES.map(function (mes, i) {
      var v = valores ? valores[i] : [0, 0, 0];
      return {
        mes: mes,
        apurado: { dic: v[0], fic: v[1], dmic: v[2] },
        limite: { dic: LIMITES.dic, fic: LIMITES.fic, dmic: LIMITES.dmic }
      };
    });
  }

  window.INDICADORES_DADOS = {
    uc: {
      codigoCliente: "••••••",
      cpf: "•••.•••.•••-••",
      endereco: "•••••••••••••••••••••••",
      unidadeConsumidora: "•••••••",
      situacao: "ATIVA"
    },
    cenarios: {
      real: {
        rotulo: "Dados reais da UC avaliada (sem interrupções)",
        registros: serie(null)
      },
      ficticio: {
        rotulo: "Dados fictícios: meses com um e com dois indicadores acima do limite",

        registros: serie([
          [0, 0, 0],
          [1.5, 1, 1.5],
          [3.25, 2, 2.5],
          [9.4, 2, 6.2],
          [2, 2, 1.25],
          [0, 0, 0],
          [8, 5, 3],
          [0, 0, 0],
          [2, 4, 0.75],
          [0.5, 1, 0.5],
          [5.5, 3, 3.5],
          [1.2, 1, 1.2]
        ])
      }
    }
  };
})();

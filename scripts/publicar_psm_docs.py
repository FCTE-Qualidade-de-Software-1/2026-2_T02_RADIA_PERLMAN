
from pathlib import Path
import shutil

ORIGEM = Path("relatorios/psm")
DESTINO = Path("docs/fase2/psm")

PASTAS = ("entrega_1", "entrega_2", "consolidado")


def main():
    if not ORIGEM.exists():
        raise SystemExit(
            "Relatórios não encontrados. Execute primeiro a coleta PSM."
        )

    DESTINO.mkdir(parents=True, exist_ok=True)

    for nome in PASTAS:
        origem = ORIGEM / nome
        destino = DESTINO / nome

        if not origem.exists():
            raise SystemExit(f"Pasta não encontrada: {origem}")

        if destino.exists():
            shutil.rmtree(destino)

        shutil.copytree(origem, destino)
        print(f"Copiado: {origem} -> {destino}")

    indice = ORIGEM / "relatorio.md"

    if not indice.exists():
        raise SystemExit(f"Arquivo não encontrado: {indice}")

    shutil.copy2(indice, DESTINO / "index.md")

    print("Documentação PSM/CID preparada com sucesso!")


if __name__ == "__main__":
    main()

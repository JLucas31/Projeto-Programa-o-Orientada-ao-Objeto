import json
import os


class JsonManager:

    @staticmethod
    def carregar(caminho: str) -> list:

        if not os.path.exists(caminho):
            return []

        with open(
            caminho,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    @staticmethod
    def salvar(caminho: str, dados: list) -> None:

        with open(caminho, "w", encoding="utf-8") as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )
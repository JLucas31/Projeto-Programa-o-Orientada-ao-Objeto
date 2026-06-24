from src.plano import Plano


class PlanoFree(Plano):

    def limite_downloads(self) -> int:
        return 0

    def qualidade_audio(self) -> str:
        return "AAC 128kbps"

    def exibir_beneficios(self) -> list[str]:
        return [
            "Com anúncios",
            "Sem download",
            "Qualidade básica"
        ]

    def __str__(self):
        return "Plano Free"
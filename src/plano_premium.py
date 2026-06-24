from src.plano import Plano


class PlanoPremium(Plano):

    def limite_downloads(self) -> int:
        return -1

    def qualidade_audio(self) -> str:
        return "FLAC 44.1kHz 16-bit"

    def exibir_beneficios(self) -> list[str]:
        return [
            "Sem anúncios",
            "Downloads ilimitados",
            "Qualidade Hi-Fi"
        ]

    def __str__(self):
        return "Plano Premium"
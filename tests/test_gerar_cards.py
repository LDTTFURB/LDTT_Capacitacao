import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


GERADOR = Path(__file__).resolve().parents[1] / "scripts" / "gerar_cards.py"


class GerarCardsTest(unittest.TestCase):
    def setUp(self):
        self.temporario = tempfile.TemporaryDirectory(
            prefix=".test-cards-", dir=GERADOR.parents[1]
        )
        self.base = Path(self.temporario.name).resolve()
        self.assertTrue(self.base.is_relative_to(GERADOR.parents[1]))
        self.addCleanup(self.temporario.cleanup)
        self.trilha = self.base / "docs/trilhas/tutoriais/Servidor"
        self.trilha.mkdir(parents=True)
        self.indice = self.trilha / "index.md"
        self.indice.write_text(
            "---\ntitle: Servidor\ndescription: Linux e Docker.\ntags: [Servidor]\n---\n",
            encoding="utf-8",
        )
        self.pagina = self.base / "docs/trilhas/index.md"
        self.pagina.write_text("Página anterior", encoding="utf-8")

    def gerar(self):
        return subprocess.run(
            [sys.executable, str(GERADOR)],
            cwd=self.base,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_nova_trilha_abre_conteudo_sem_alterar_metadados(self):
        self.trilha.joinpath("conteudo.md").write_text("# Servidor\n", encoding="utf-8")
        metadados = self.indice.read_bytes()
        resultado = self.gerar()
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        pagina = self.pagina.read_text(encoding="utf-8")
        self.assertIn('href="tutoriais/Servidor/conteudo/"', pagina)
        self.assertNotIn('href="tutoriais/Servidor/"', pagina)
        self.assertEqual(self.indice.read_bytes(), metadados)

    def test_trilha_incompleta_interrompe_geracao(self):
        resultado = self.gerar()
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("conteudo.md", resultado.stderr)
        self.assertIn("Servidor", resultado.stderr)
        self.assertEqual(self.pagina.read_text(encoding="utf-8"), "Página anterior")


if __name__ == "__main__":
    unittest.main()

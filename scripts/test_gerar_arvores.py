import contextlib
import io
from pathlib import Path
import tempfile
import unittest

import yaml
import gerar_arvores


class TestHierarquia(unittest.TestCase):
    def no(self, titulo, pai, nivel, ordem=0):
        return dict(card=f'<a>{titulo}</a>', pai=pai, nivel=nivel, ordem=ordem)

    def test_audio_e_interface_sao_filhos_de_unity(self):
        nos = {
            'geral': self.no('Geral', None, 0),
            'unity': self.no('Unity', 'geral', 1),
            'git': self.no('Git', 'geral', 1, 1),
            'audio': self.no('Áudio', 'unity', 2, 1),
            'interface': self.no('Interface', 'unity', 2, 0),
        }
        html = gerar_arvores.montar_hierarquia(nos)
        unity = html.split('data-id="unity"', 1)[1].split('data-id="git"', 1)[0]
        self.assertIn('data-id="audio" data-nivel="2"', unity)
        self.assertIn('data-id="interface" data-nivel="2"', unity)
        self.assertLess(unity.index('<a>Interface'), unity.index('<a>Áudio'))
        self.assertEqual(html.count('data-nivel="1"'), 2)

    def test_rejeita_pai_ausente_ciclos_multiplas_raizes_e_nivel_incorreto(self):
        casos = [
            {'a': self.no('A', 'inexistente', 1)},
            {'a': self.no('A', 'b', 0), 'b': self.no('B', 'a', 1)},
            {'a': self.no('A', None, 0), 'b': self.no('B', None, 0)},
            {'a': self.no('A', None, 0), 'b': self.no('B', 'a', 2)},
            {'a': self.no('A', None, 0), 'b': dict(card='B', nivel=1, ordem=0)},
        ]
        for nos in casos:
            with self.subTest(nos=nos), self.assertRaises(ValueError):
                gerar_arvores.montar_hierarquia(nos)

    def test_processamento_mantem_url_e_exibe_csharp_sem_barra(self):
        with tempfile.TemporaryDirectory() as temp:
            trilha = Path(temp) / 'unity'
            material = trilha / 'materiais' / 'introducao'
            material.mkdir(parents=True)
            (trilha / 'index.md').write_text('---\ntitle: Unity\n---\n', encoding='utf-8')
            pagina = trilha / 'conteudo.md'
            pagina.write_text('# Mapa\n\n<!-- GERAR_CARDS -->', encoding='utf-8')
            dados = dict(title=r'Introdução ao C\#', description='Aprenda', pai=None,
                         nivel=0, ordem=0, destino='conteudo.md')
            (material / 'index.md').write_text('---\n' + yaml.safe_dump(dados) + '---\n', encoding='utf-8')
            (material / 'conteudo.md').write_text('# Introdução', encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                gerar_arvores.processar_trilha(trilha)
            html = pagina.read_text(encoding='utf-8')
            self.assertIn('<strong>Introdução ao C#</strong>', html)
            self.assertIn('/LDTT_Capacitacao/trilhas/tutoriais/unity/materiais/introducao/conteudo/', html)

    def test_trilhas_sem_pai_mantem_apresentacao_por_niveis(self):
        html = gerar_arvores.montar_arvore({0: [(0, 'raiz', '<a>Raiz</a>')],
                                           1: [(0, 'filho', '<a>Filho</a>')]})
        self.assertNotIn('arvore-hierarquia', html)
        self.assertLess(html.index('<a>Raiz'), html.index('<a>Filho'))


if __name__ == '__main__':
    unittest.main()

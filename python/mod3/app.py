import pandas as pd
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from io import BytesIO
import logging

class MyApp(App):
    def build(self):
        
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            
        try:
            acoes = pd.read_excel("acoes_ibovespa_marco_junho.xlsx")
            logging.info("Arquivo importado com sucesso!")
        except FileNotFoundError:
            logging.error(f"Arquivo não encontrado. Certifique-se de que o arquivo {acoes} está na pasta correta.")
        except Exception as e:
            logging.error(f"Ocorreu um erro ao importar o arquivo: {acoes}")
        
        acoes = acoes.drop('Data', axis=1)
        acoes = acoes.drop('Variação', axis=1)
        acoes = acoes.drop('Variação (%)', axis=1)
        acoes = acoes.drop('Abertura', axis=1)
        acoes = acoes.drop('Máxima', axis=1)
        acoes = acoes.drop('Mínima', axis=1)
        acoes = acoes.drop('Volume', axis=1)

        acoes_marco = acoes[acoes["Mes"]=="MARCO"].groupby('Acoes').sum()
        acoes_marco.sort_values(by='Fechamento')
        acoes_marco = acoes_marco.rename(columns={'Fechamento': 'MARCO'})

        acoes_abril = acoes[acoes["Mes"]=="ABRIL"].groupby('Acoes').sum()
        acoes_abril.sort_values(by='Fechamento')
        acoes_abril = acoes_abril.rename(columns={'Fechamento': 'ABRIL'})

        acoes_maio = acoes[acoes["Mes"]=="MAIO"].groupby('Acoes').sum()
        acoes_maio.sort_values(by='Fechamento')
        acoes_maio = acoes_maio.rename(columns={'Fechamento': 'MAIO'})

        acoes_junho = acoes[acoes["Mes"]=="JUNHO"].groupby('Acoes').sum()
        acoes_junho.sort_values(by='Fechamento')
        acoes_junho = acoes_junho.rename(columns={'Fechamento': 'JUNHO'})

        acoes_mes_a_mes = pd.concat([acoes_marco, acoes_abril, acoes_maio, acoes_junho], axis=1)
        acoes_mes_a_mes['MEDIA 4 MESES'] = acoes_mes_a_mes.mean(axis=1).round(2)
        exibir = acoes_mes_a_mes.sort_values(by='MEDIA 4 MESES', ascending=False).head(10)

        layout = BoxLayout(orientation='vertical')
        label = Label(text=str(exibir), font_size='12sp', padding=10)
        layout.add_widget(label)

        plt.figure(figsize=(10, 6))
        plt.bar(exibir, 16, color='blue')
        plt.xlabel('Acoes')
        plt.ylabel('MEDIA 4 MESES')
        plt.title('Top 10 Acoes nos últimos 4 meses')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        self.image_texture = Texture.create(size=(plt.gcf().bbox.width, plt.gcf().bbox.height))
        self.image_texture.blit_buffer(image_stream.getvalue(), colorfmt='rgba', bufferfmt='ubyte')
        
        imagem = Image(texture=self.image_texture, size_hint=(1, None), height=300)
        layout.add_widget(imagem)

        return layout

if __name__ == "__main__":
    MyApp().run()
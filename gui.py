import gradio as gr
from gpt import Model  

M = Model()

def query(name):
    M.set(name)
    return M.get_answer()

textbox_input = gr.Textbox(show_label = False, placeholder = "Введите ваше сообщение ...", container = False)

demo = gr.Interface(fn=query, inputs=[textbox_input, "image", gr.Dropdown(["Завтрак", "Обед", "Ужин"], label="А когда кушать то..?",)], outputs=[gr.Textbox(label="Книга рецептов YandexGPT", lines=3), gr.Dataframe(label="<Холодильник>")])
with demo:
    gr.Markdown(
        """
    # Приветсвуем в GPT.Рецепты!
    По вопросам работы приожения просьба НЕ обращатся по телефону:
    +7 999 999 9999
    """
    )

demo.launch(share=True)
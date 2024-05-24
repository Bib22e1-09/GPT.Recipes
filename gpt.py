import requests
import json

class Model:
    prompt = {
    "modelUri": "gpt://ajeiokji72ng2gms1bmf/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "user",
            "text": "Твоя роль - профессиональный повар. В твоем распоряжении есть [морковь, сельдерей, рис, хлеб]. Опиши шаг за шагом рецепт,только из этих ингредиентов, для [Завтрак]. Размер статьи - 500 до 700 символов.'"
        }
    ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN0sUnI4rwFC3Ars_mzWM8-6-Bsy2u_SuNRO5L"
    }

    def set(self,text):
        self.prompt["messages"][0]["text"] = text

    def __parse_text(self,text_from_server):
        data = json.loads(text_from_server)
        text = data["result"]["alternatives"][0]["message"]["text"]
        print (text)
        return text


    def get_answer(self):
        response = requests.post(self.url, headers=self.headers, json=self.prompt)
        result = response.text
        return self.__parse_text(result)

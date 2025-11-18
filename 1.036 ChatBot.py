import random

class AdvancedChatBot:
    def __init__(self):
        self.running = True
        self.responses = {
            "hola": ["Hola", "Como estas?", "Buen día", "¿En qué puedo ayudarte?"],
            "adios": ["Adios", "Hasta luego", "Cuídate", "Nos vemos pronto"],
            "como estas": ["Estoy bien", "Muy bien, gracias", "¿Y tú?"],
            "cual es tu funcion": ["Mi función es responder tus preguntas", "Estoy aquí para ayudarte"]
        }

        self.default_response = [
            "No estoy seguro cómo responder eso",
            "¿Podrías intentar otra pregunta?",
            "Lo siento, aún estoy aprendiendo"
        ]

    def iniciar_chat(self):
        print("Soy ChatBox Avanzado. Escribe 'salir' para finalizar.")

        while self.running:
            user_message = input("Usuario: ").strip().lower()

            if user_message == "salir":
                self.running = False
                print("ChatBox finalizado. ¡Hasta luego!")
            else:
                bot_message = self.generate_responses(user_message)
                print("Bot:", bot_message)

    def generate_responses(self, user_message):
        # Buscar coincidencias
        for keyword, response_list in self.responses.items():
            if keyword in user_message:
                return random.choice(response_list)

        # Si no encuentra coincidencia
        return random.choice(self.default_response)


if __name__ == "__main__":
    chatbot = AdvancedChatBot()
    chatbot.iniciar_chat()

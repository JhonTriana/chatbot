from chatterbot import ChatBot

chatbot = ChatBot(
    "conchita",

    storage_adapter= 'chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://localhost:27017',
    database='chatterbot_conchita',

    input_adapter="chatterbot.input.TerminalAdapter",

    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response" 
        },
        {
            'import path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.51,
            'default_response': 'Disculpa no entendi bien, ¿Puedes ser más específic@?'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': '¿Quiero saber si quedan cupos?',
            'output_text': 'Puedes averigualo en la pagina de la Secretaria de Educación: https://www.educacionbogota.edu.co/portal_institucional/'
        },
    ],

    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],

    read_only=True,
)
DEFAULT_SESSION_ID = chatbot.default_session.id

from chatterbot.trainers import chatterbotCorpusTrainer

chatbot.set_trainer(chatterbotCorpusTrainer)
chatbot.train("conchita_ES.yml")

while True:
    input_statement = chatbot.input_process_input_statement()
    statement, response = chatbot.generate_response(input_statement, DEFAULT_SESSION_ID)
    print("\n%s\n\n" % response)
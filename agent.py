from dotenv import load_dotenv
from crewai import Agent, Task

load_dotenv()

agent = Agent(
    role="PipoAgent",
    goal="Responder perguntas gerais sobre qualquer assunto",
    backstory="Você se chama PipoAgent por causa do meu amigo Pipokin que estava assistindo enquanto eu te criava.",
    llm="gpt-4o-mini",
    verbose=True
)

task = Task(
    description="Bom dia!",
    expected_output="Resposta objetiva"
)

output = agent.execute_task(task=task)

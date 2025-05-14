Iai, galerinha, beleza? ☕
Aqui eu vou mostrar como criar o **seu primeiro agente** com CrewAI, passo a passo! 🚀

---

**1. Instalar o Python (≥ 3.10 e < 3.13)**
Verifique a versão instalada:

```bash
python3 --version
```

Se o número não bater, baixe em:
🔗 [https://www.python.org/downloads](https://www.python.org/downloads)

**2. Build Tools (Windows)**
No Windows, é preciso o **Visual Studio Build Tools – C++**:

1. Acesse 🔗 [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Selecione “Desktop development with C++”

**3. Criar e ativar o ambiente virtual**

Windows (PowerShell)

```powershell
python -m venv venv  
source venv\Scripts\activate
```

MacOS/Linux

```bash
python3 -m venv venv  
source venv/bin/activate
```

Isso isola suas libs e evita instalar muita coisa no seu computador. 
É bom, confia. 👌🏻

**4. Instalar CrewAI + Extras**

```bash
pip install crewai crewai-tools  
crewai --version
```

Você deve ver algo como `crewai, version x.y.z`

**5. Configurar sua API Key**
Na raiz do projeto, crie um arquivo `.env` com:

```dotenv
OPENAI_API_KEY="sua_chave_aqui"
```

Sem ele, nada funciona!


## 🚀 6. Criando o seu FirstAgent

Crie um arquivo `agent.py` e cole:

```python
from dotenv import load_dotenv
from crewai import Agent, Task

load_dotenv()

agent = Agent(
    role="FirstAgent",
    goal="Responder perguntas gerais sobre qualquer assunto",
    backstory="Você se chama FirstAgent e foi criado para mostrar como criar agentes no LinkedIn.",
    llm="gpt-4o-mini",
    verbose=True
)

task = Task(
    description="Bom dia!",
    expected_output="Resposta objetiva"
)

output = agent.execute_task(task=task)
print(output)
```

Em seguida, no terminal:

```bash
python agent.py
```

E voilà: seu agente responde rapidinho! 🎉

---

**Links úteis:**

🔗 Docs CrewAI: [https://docs.crewai.com](https://docs.crewai.com)

🔗 PyPI CrewAI: [https://pypi.org/project/crewai](https://pypi.org/project/crewai)

🔗 GitHub Tools: [https://github.com/crewai/crewai-tools](https://github.com/crewai/crewai-tools)

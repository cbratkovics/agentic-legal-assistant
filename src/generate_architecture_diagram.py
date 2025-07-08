from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.general import User
from diagrams.programming.flowchart import InputOutput, Decision
from diagrams.generic.network import Firewall
from diagrams.generic.blank import Blank

with Diagram("LangGraph Legal Assistant", filename="outputs/architecture_diagram", outformat="png", show=True, direction="TB"):
    with Cluster("Legend", graph_attr={"fontsize": "9", "style": "filled", "color": "#EAF6FB", "pencolor": "#EAF6FB", "bgcolor": "#EAF6FB", "margin": "10"}):
        l_user = User("User")
        l_input = InputOutput("Input")
        l_agent = Decision("Agent")
        l_tool = Custom("Tool", "./assets/openai.png")
        l_result = Firewall("Result")

    user = User("User Input")
    question = InputOutput("Input:\nLegal Question")
    agent = Decision("Chat Agent\n(LLM Decision)")
    tool = Custom("Tool Node\n(Retriever)", "./assets/openai.png")
    result = Firewall("Return Context\nLangGraph Legal Assistant")
    answer = Blank("Grounded Answer")

    user >> Edge(color="#2E86AB", minlen="2") >> question
    question >> Edge(color="#2E86AB", minlen="2") >> agent
    agent >> Edge(label="1. Calls Tool", color="#E67E22", minlen="2", fontsize="10") >> tool
    tool >> Edge(label="2. Returns Context", color="#E67E22", minlen="2", fontsize="10") >> result
    result >> Edge(label="3. Sends Back to Agent", color="#E67E22", minlen="2", fontsize="10") >> agent
    agent >> Edge(label="4. Final Answer", color="#27AE60", minlen="2", fontsize="10") >> answer

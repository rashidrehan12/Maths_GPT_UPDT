# # import streamlit as st
# # from langchain_groq import ChatGroq
# # from langchain.chains import LLMMathChain, LLMChain
# # from langchain.prompts import PromptTemplate
# # from langchain_community.utilities import WikipediaAPIWrapper
# # from langchain.agents.agent_types import AgentType
# # from langchain.agents import Tool, initialize_agent
# # from langchain.callbacks import StreamlitCallbackHandler

# # ## Set upi the Stramlit app
# # st.set_page_config(page_title="Text To MAth Problem Solver And Data Serach Assistant",page_icon="🧮")
# # st.title("Text To Math Problem Solver Using Google Gemma 2")

# # groq_api_key=st.sidebar.text_input(label="Groq API Key",type="password")


# # if not groq_api_key:
# #     st.info("Please add your Groq APPI key to continue")
# #     st.stop()

# # llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)


# # ## Initializing the tools
# # wikipedia_wrapper=WikipediaAPIWrapper()
# # wikipedia_tool=Tool(
# #     name="Wikipedia",
# #     func=wikipedia_wrapper.run,
# #     description="A tool for searching the Internet to find the vatious information on the topics mentioned"

# # )

# # ## Initializa the MAth tool

# # math_chain=LLMMathChain.from_llm(llm=llm)
# # calculator=Tool(
# #     name="Calculator",
# #     func=math_chain.run,
# #     description="A tools for answering math related questions. Only input mathematical expression need to bed provided"
# # )

# # prompt="""
# # Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
# # and display it point wise for the question below
# # Question:{question}
# # Answer:
# # """

# # prompt_template=PromptTemplate(
# #     input_variables=["question"],
# #     template=prompt
# # )

# # ## Combine all the tools into chain
# # chain=LLMChain(llm=llm,prompt=prompt_template)

# # reasoning_tool=Tool(
# #     name="Reasoning tool",
# #     func=chain.run,
# #     description="A tool for answering logic-based and reasoning questions."
# # )

# # ## initialize the agents

# # assistant_agent=initialize_agent(
# #     tools=[wikipedia_tool,calculator,reasoning_tool],
# #     llm=llm,
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     verbose=False,
# #     handle_parsing_errors=True
# # )

# # if "messages" not in st.session_state:
# #     st.session_state["messages"]=[
# #         {"role":"assistant","content":"Hi, I'm a MAth chatbot who can answer all your maths questions"}
# #     ]

# # for msg in st.session_state.messages:
# #     st.chat_message(msg["role"]).write(msg['content'])

# # ## LEts start the interaction
# # question=st.text_area("Enter your question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

# # if st.button("find my answer"):
# #     if question:
# #         with st.spinner("Generate response.."):
# #             st.session_state.messages.append({"role":"user","content":question})
# #             st.chat_message("user").write(question)

# #             st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
# #             response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb]
# #                                          )
# #             st.session_state.messages.append({'role':'assistant',"content":response})
# #             st.write('### Response:')
# #             st.success(response)

# #     else:
# #         st.warning("Please enter the question")











# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain.chains import LLMMathChain, LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import WikipediaAPIWrapper
# from langchain.agents.agent_types import AgentType
# from langchain.agents import Tool, initialize_agent
# from langchain.callbacks import StreamlitCallbackHandler

# # Set up Streamlit app
# st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
# st.title("Text To Math Problem Solver Using Google Gemma 2")

# groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

# if not groq_api_key:
#     st.info("Please add your Groq API key to continue")
#     st.stop()

# llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# # Initializing the tools
# wikipedia_wrapper = WikipediaAPIWrapper()
# wikipedia_tool = Tool(
#     name="Wikipedia",
#     func=wikipedia_wrapper.run,
#     description="A tool for searching the Internet to find various information on the topics mentioned"
# )

# # Initialize the Math tool
# math_chain = LLMMathChain.from_llm(llm=llm)
# calculator = Tool(
#     name="Calculator",
#     func=math_chain.run,
#     description="A tool for answering math-related questions. Only input mathematical expressions need to be provided"
# )

# prompt = """
# You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide a detailed explanation
# and display it point-wise for the question below
# Question: {question}
# Answer:
# """

# prompt_template = PromptTemplate(
#     input_variables=["question"],
#     template=prompt
# )

# # Combine all the tools into a chain
# chain = LLMChain(llm=llm, prompt=prompt_template)

# reasoning_tool = Tool(
#     name="Reasoning tool",
#     func=chain.run,
#     description="A tool for answering logic-based and reasoning questions."
# )

# # Initialize the agent
# assistant_agent = initialize_agent(
#     tools=[wikipedia_tool, calculator, reasoning_tool],
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=False,
#     handle_parsing_errors=True
# )

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [
#         {"role": "assistant", "content": "Hi, I'm a math chatbot who can answer all your math questions"}
#     ]

# # Display chat history
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg['content'])

# # Interaction options
# question = st.text_area("Enter your question:", "")

# # Option to choose the type of question
# question_type = st.selectbox(
#     "Select the type of question:",
#     ["Math Problem", "General Information"]
# )

# if st.button("Find My Answer"):
#     if question:
#         with st.spinner("Generating response..."):
#             st.session_state.messages.append({"role": "user", "content": question})
#             st.chat_message("user").write(question)

#             st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            
#             if question_type == "Math Problem":
#                 response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
#             else:
#                 response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

#             st.session_state.messages.append({'role': 'assistant', "content": response})
#             st.write('### Response:')
#             st.success(response)

#     else:
#         st.warning("Please enter a question")

# # Add Clear Chat History button
# if st.sidebar.button("Clear Chat History"):
#     st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I'm a math chatbot who can answer all your math questions"}]
#     st.experimental_rerun()

# # Optional: Display chat history in the sidebar
# if st.sidebar.checkbox("Show Chat History"):
#     st.sidebar.subheader("Chat History")
#     for i, msg in enumerate(st.session_state.messages):
#         st.sidebar.write(f"{i+1}: {msg['role']} - {msg['content']}")





# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain.chains import LLMMathChain, LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities import WikipediaAPIWrapper
# from langchain.agents.agent_types import AgentType
# from langchain.agents import Tool, initialize_agent
# from langchain.callbacks import StreamlitCallbackHandler

# # Set up Streamlit app with custom theme
# st.set_page_config(
#     page_title="Math Solver & Data Search Assistant",
#     page_icon="🧮",
#     layout="centered",  # centered layout for a more balanced view
#     initial_sidebar_state="expanded",
# )

# # Custom CSS for a cleaner look
# st.markdown("""
#     <style>
#         body {
#             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#         }
#         .stButton button {
#             background-color: #007BFF;
#             color: white;
#             border-radius: 4px;
#             margin: 10px 0px;
#             font-size: 16px;
#             padding: 10px 20px;
#         }
#         .stButton button:hover {
#             background-color: #0056b3;
#         }
#         .stTextInput input {
#             font-size: 16px;
#         }
#         .stTextArea textarea {
#             font-size: 16px;
#         }
#         .stSelectbox select {
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.title("🧮 Math Solver & Data Search Assistant")
# st.write("Effortlessly solve complex math problems or search for information using advanced AI tools.")

# # Sidebar for API key input
# st.sidebar.header("API Key")
# groq_api_key = st.sidebar.text_input(
#     label="Enter your Groq API Key:",
#     type="password",
#     help="You need a valid Groq API key to use this app."
# )

# if not groq_api_key:
#     st.sidebar.warning("Please enter your Groq API key to continue.")
#     st.stop()

# # Initialize the LLM
# llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# # Initialize tools
# wikipedia_wrapper = WikipediaAPIWrapper()
# wikipedia_tool = Tool(
#     name="Wikipedia",
#     func=wikipedia_wrapper.run,
#     description="Search Wikipedia for relevant information."
# )

# math_chain = LLMMathChain.from_llm(llm=llm)
# calculator = Tool(
#     name="Calculator",
#     func=math_chain.run,
#     description="Solve math problems by entering mathematical expressions."
# )

# prompt_template = PromptTemplate(
#     input_variables=["question"],
#     template="""
#     You are an AI assistant tasked with solving users' mathematical questions. Provide a clear, step-by-step solution:
#     Question: {question}
#     Answer:
#     """
# )

# chain = LLMChain(llm=llm, prompt=prompt_template)

# reasoning_tool = Tool(
#     name="Reasoning Tool",
#     func=chain.run,
#     description="Answer logic-based and reasoning questions."
# )

# assistant_agent = initialize_agent(
#     tools=[wikipedia_tool, calculator, reasoning_tool],
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=False,
#     handle_parsing_errors=True
# )

# # Chat history management
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm here to help with math problems and information searches."}]

# # Display chat history in a container
# with st.container():
#     for msg in st.session_state.messages:
#         st.chat_message(msg["role"]).markdown(msg['content'])

# # Input form for new questions
# with st.form(key="question_form"):
#     question = st.text_area(
#         "Enter your question:",
#         placeholder="Example: What is the square root of 144? How many fruits will I have after giving away 2 apples?",
#         height=100
#     )

#     question_type = st.selectbox(
#         "Select the type of question:",
#         ["Math Problem", "General Information"],
#         help="Choose 'Math Problem' for calculations or 'General Information' for factual searches."
#     )

#     submit_button = st.form_submit_button("Get Answer")

# if submit_button and question:
#     with st.spinner("Generating response..."):
#         st.session_state.messages.append({"role": "user", "content": question})
#         st.chat_message("user").markdown(question)

#         st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

#         response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
#         st.session_state.messages.append({'role': 'assistant', "content": response})

#         st.chat_message("assistant").markdown(response)

# # Sidebar: Clear chat history
# if st.sidebar.button("Clear Chat History"):
#     st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm here to help with math problems and information searches."}]
#     st.experimental_rerun()

# # Sidebar: Show chat history option
# if st.sidebar.checkbox("Show Chat History"):
#     st.sidebar.subheader("Chat History")
#     for i, msg in enumerate(st.session_state.messages):
#         st.sidebar.write(f"{i + 1}. **{msg['role'].capitalize()}**: {msg['content']}")




import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# Set up Streamlit app with custom theme
st.set_page_config(
    page_title="Math Solver & Data Search Assistant",
    page_icon="🧮",
    layout="centered",  # centered layout for a more balanced view
    initial_sidebar_state="expanded",
)

# Custom CSS for a cleaner look
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
            border-radius: 4px;
            margin: 10px 0px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .stTextInput input {
            font-size: 16px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stSelectbox select {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🧮 Math Solver & Data Search Assistant")
st.write("Effortlessly solve complex math problems or search for information using advanced AI tools.")

# Sidebar for API key input
st.sidebar.header("API Key")
groq_api_key = st.sidebar.text_input(
    label="Enter your Groq API Key:",
    type="password",
    help="You need a valid Groq API key to use this app."
)

if not groq_api_key:
    st.sidebar.warning("Please enter your Groq API key to continue.")
    st.stop()

# Initialize the LLM
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Search Wikipedia for relevant information."
)

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="Solve math problems by entering mathematical expressions."
)

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
    You are an AI assistant tasked with solving users' mathematical questions. Provide a clear, step-by-step solution:
    Question: {question}
    Answer:
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="Answer logic-based and reasoning questions."
)

assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Chat history management
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm here to help with math problems and information searches."}]

# Display chat history in a container
with st.container():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg['content'])

# Input form for new questions
with st.form(key="question_form"):
    question = st.text_area(
        "Enter your question:",
        placeholder="Example: What is the square root of 144? How many fruits will I have after giving away 2 apples?",
        height=100
    )

    question_type = st.selectbox(
        "Select the type of question:",
        ["Math Problem", "General Information"],
        help="Choose 'Math Problem' for calculations or 'General Information' for factual searches."
    )

    submit_button = st.form_submit_button("Get Answer")

if submit_button and question:
    with st.spinner("Generating response..."):
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").markdown(question)

        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role': 'assistant', "content": response})

        st.chat_message("assistant").markdown(response)

# Sidebar: Clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm here to help with math problems and information searches."}]
    st.experimental_rerun()

# Sidebar: Show chat history option
if st.sidebar.checkbox("Show Chat History"):
    st.sidebar.subheader("Chat History")
    for i, msg in enumerate(st.session_state.messages):
        st.sidebar.write(f"{i + 1}. **{msg['role'].capitalize()}**: {msg['content']}")


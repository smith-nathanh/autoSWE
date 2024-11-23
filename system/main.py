from dotenv import load_dotenv
import os
import logging
from langsmith import utils
from langchain_core.messages import HumanMessage
from graph import build_graph
from prompts import SAMPLE_PRD, DESIGN_PROMPT
import argparse


# set logging level
logging.basicConfig(level=logging.INFO)


def main():
    """
    Main entry point to invoke the graph.
    """
    parser = argparse.ArgumentParser(description="Run the graph with a specified PRD.")
    parser.add_argument("--prd_path", type=str, default=None, help="Path to the PRD file")
    args = parser.parse_args()

    if args.prd_path is None:
        prd_content = SAMPLE_PRD
    else:
        with open(args.prd_path, 'r', encoding="utf-8") as prd_file:
            prd_content = prd_file.read()

    graph = build_graph()
    graph.get_graph().draw_mermaid_png(output_file_path="images/swegraph.png")
    state = {'documents': {'PRD': prd_content},
             'messages': [HumanMessage(content=DESIGN_PROMPT.format(PRD=prd_content))]}
    final_state = graph.invoke(state)


if __name__ == "__main__":
    load_dotenv(dotenv_path=".env", override=True)
    logging.info('TRACING %s', str(utils.tracing_is_enabled()))
    logging.info(os.environ["LANGCHAIN_PROJECT"])
    main()

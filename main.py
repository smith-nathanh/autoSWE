from dotenv import load_dotenv
import os
import logging
from langsmith import utils
from langchain_openai import ChatOpenAI
from graph import build_graph
from prompts import SAMPLE_PRD
import argparse


# set logging level
logging.basicConfig(level=logging.INFO)


def main():
    """
    Main entry point to invoke the SWEGraph.
    """
    parser = argparse.ArgumentParser(description="Run the SWEGraph with a specified PRD.")
    parser.add_argument("--prd_path", type=str, default=None, help="Path to the PRD file")
    args = parser.parse_args()

    if args.prd_path is None:
        prd_content = SAMPLE_PRD
    else:
        with open(args.prd_path, 'r') as prd_file:
            prd_content = prd_file.read()

    graph = build_graph()
    graph.get_graph().draw_mermaid_png(output_file_path="images/swegraph.png")
    graph.invoke({"documents": {'PRD': prd_content}})


if __name__ == "__main__":
    load_dotenv(dotenv_path=".env", override=True)
    logging.info('TRACING %s', str(utils.tracing_is_enabled()))
    logging.info(os.environ["LANGCHAIN_PROJECT"])
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    main()

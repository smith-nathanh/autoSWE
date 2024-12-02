
# using structured outputs
# having trouble getting implementation prompt to work with anthropic model
# need to refine these prompts in general

SAMPLE_PRD = """
# Introduction
The purpose of this project is to develop a code repository that implements the TextCNN model for movie review sentiment classification using the PyTorch library. This repository should include all the necessary components and features to support the development of the model.
# Goals
The objective of this project is to construct and evaluate a TextCNN model using the PyTorch library for text classification. This includes the data pre-processing, the training of the model and evaluation of the model performance via accuracy.
# Features and Functionalities
The following features and functionalities are expected in the project:
- Modeling: 
    - ability to define and manage model-related settings such as kernel sizes, dimension of embedding, maximum length of sequence;
    - ability to configure model training settings such as learning rate, batch size, number of epochs;
    - ability to define the custom parameter during training such as number of epoch to save model and number of batch to log training loss;
    - ability to save the model checkpoint with the highest evaluation accuracy during training;
    - ability to reproduce the training and testing results when random seeds are fixed.
    - ability to log training loss and accuracy for every k batches;
    - ability to log loss and accuracy for both train and validation sets for each epoch;
    - ability to calculate the accuracy of model output on test dataset;
    - ability to construct the TextCNN model using PyTorch, where the structure of a TextCNN model consists of an embedding layer, a series of convolutional layers, a maximum pooling layer, relu activation function, and a fully connected layer in a fixed order.
- Data:
    - ability to load and pre-process the IMDb dataset from HuggingFace datasets;
    - ability to load `bert-base-uncased` tokenizer from HuggingFace transformers to convert text into vectors;
    - ability to split the train dataset into train and validation sets, specify the split ratio to 0.1.
- Examples:
    - example scripts to run the code for both training and testing.
# Technical Constraints
- The repository should support building modeling frameworks using pytorch. 
- The repository should support training model using pytorch instead of the trainer api of transformers.
# Requirements
## Dependencies
- transformers library
- datasets library
- evaluate library
- PyTorch library
# Usage
To train a model, run the following script
```bash
python main.py \
  --learning_rate 0.01 \
  --num_epochs 10 \
  --batch_size 16 \
  --embedding_dim 300\
  --kernel_sizes 3 4 5\
  --max_length 50\
  --save_every_n_epoch 2\
  --train \
  --gpu \
  --output_dir './outputs'\
  --train_log_per_k_batch 20\
  --random_seed 20
```
To test a trained checkpoint in a specified `output_dir`, run the following script. 
```bash
python main.py \
  --test \
  --gpu \
  --output_dir './outputs'
```
## Command Line configuration arguments
 - learning_rate (float, optional) - A value representing the learning rate for training, with a default value of 1e-3.
 - batch_size (int, optional) - A value representing the batch size for training, with a default value of 32.
 - num_epochs (int, optional) - A value representing the number of epochs for training, with a default value of 10.
 - embedding_dim (int, optional) - A value representing the number of neurons in the layer, with a default value of 500.
 - kernel_sizes (lis, optional) - A list of values representing the kernel sizes, with a default value of [3, 4, 5].
 - max_length (int, optional) - A value representing the maximum length of sentences, with a default value of 50.
 - save_every_n_epoch (int, optional) - A value representing the number of epochs to save the model, with a default value of 1.
 - train (Boolean, optional) - A boolean value representing whether to train the model, with a default value of FALSE.
 - test (Boolean, optional) - A boolean value representing whether to test the model, with a default value of FALSE.
 - output_dir (str, required) - A string value representing the path to output directory.
 - gpu (Boolean, optional) - A boolean value representing whether to use GPU, with a default value of FALSE.
 - train_log_per_k_batch (int, optional) - A value representing the number of batch to log the training loss, with a default value of 10.
 - random_seed (int, optional) - A value representing the random seed, with a default value of 42.
# Acceptance Criteria
The repository should cover acceptance testing for both training and testing modes, by setting command line parameter to `--train` and `--test`.
- For the training mode, the model training logs will be tested if the training loss decreases between the first epoch and the last epoch, and if the accuracy of the model evaluation results is above 0.6.
- For the testing mode, the terminal output will be tested whether the accuracy of the given trained model on the test dataset is above 0.6.
# Terms/Concepts Explanation
TextCNN (Convolutional Neural Networks for Text Classification) is a convolutional neural network model introduced by Yoon Kim in 2014. It works by constructing and training a convolutional neural network (CNN) model to classify text into predefined labels. The model performs well and is considered one of the widely applicable architectures for text classification. The IMDb dataset is a collection of over 25000 movie reviews from users on the Internet Movie Database website. The dataset is typically used to train or test machine learning models for movie sentiment analysis.
"""


DESIGN_PROMPT = """
Consider the following product requirements document (PRD)

PRD
-----------
{PRD}


-----Instructions------
Using the PRD as a source of truth and guideline, I am going to ask you to generate some specific artifacts.
Do not suggest in your design that we should import a package that already does the things in the PRD. I want to generate code that performs the things outlined in the PRD from scratch.
Based on the specifications outlined in the PRD document, return a dictionary with the following keys:
1. UML_class: A Mermaid 11 class diagram that reflects the class structure and relationships defined in the PRD
2. UML_sequence: A Mermaid 11 sequence diagram showing the key interactions and flow between components as specified in the PRD
3. architecture_design: A detailed text based representation of the file tree (with all files and folders under a root directory "project-root") that is true to the PRD and includes but is not limited to:
  - A README.md file documenting the system overview
  - An 'examples' directory (inside the root directory) containing:
    - example_usage.sh demonstrating core functionality along with any additional example files that align with use cases mentioned in the PRD
  - Every single file and directory MUST be connected with ASCII lines:
   - Vertical lines: │
   - Branch lines: ├───
   - Last item lines: └───
   - Each item must have a horizontal line (───) connecting to it
  - The directory structure must be clear with proper ASCII connection lines like this example:
project-root/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── config.py
└── tests/
    ├── __init__.py
    └── test_main.py
"""

APPROVE_DESIGN_PROMPT = """
You are an expert software engineer. 

Below is the evaluation criteria I want you to use to evaluate the UML_class diagram, UML_sequence diagram, and architecture_design.

```
Evaluation Guidance for UML_class
General Principles
• Cohesion and Decoupling: The design should aim for high cohesion within individual classes and low coupling
between different classes. High cohesion ensures that each class is dedicated to a singular task or concept, enhancing
clarity and functionality. Low coupling reduces dependencies among classes, facilitating easier maintenance and
scalability.
• Complexity: Utilize metrics such as the total number of classes, the average number of methods per class, and
the depth of the inheritance tree to evaluate complexity. It's important to discern between conceptual classes and
attributes; not every noun should become a class. The complexity level should be appropriately balanced, aligning
with the specific requirements detailed in the repository's Product Requirement Document (PRD).
• Practicability: A practical design should be readable and understandable, offering a clear and comprehensive representation
of the software's structures, functionalities, and behaviors. This enhances ease in programming, testing,
and maintenance. Modularity should be evident, with each component serving a distinct function, streamlining
the development process. Interfaces need to be designed for simplicity, facilitating smooth interactions within the
software and with external environments. The design must also support robust testing strategies, enabling thorough
validation through unit and acceptance tests, ensuring the design's viability in real-world applications.
Faithfulness
• Ensure that the design aligns with the given PRD strictly, achieving all the functionalities based on the requirements
without making any hallucinations and additions. Ensure that the conceptual classes and their relationships
accurately represent the essentials outlined in the PRD. This includes a detailed focus on the associations between
classes, their cardinalities, and the types of relationships such as inheritance, aggregation, and composition. Clarity
in class names and the optional inclusion of attributes are key for aligning with the repository's vision.
```
```
Evaluation Guidance for UML_sequence
General Principles
• Uniformity and Integration: The design should demonstrate a consistent style and integrated approach, ensuring all
components work seamlessly together.
• Cohesion and Decoupling: Evaluate the sequence diagram for its cohesion within sequences and coupling between
different parts of the system. The goal is to ensure each sequence is focused, with minimal dependencies between
different system components. Strive for high cohesion within sequences and low coupling between them.
• Interaction complexity: This metric assesses the interaction complexity of the sequence diagram, focusing on the
number of messages, depth of nested calls, and the number of participating objects. It also examines how the
sequence of messages and the roles of key objects are portrayed in these interactions. The ideal level of complexity
should be in line with the specific requirements detailed in the repository's PRD
• Practicability: This comprehensive metric includes aspects of readability, understandability, class and method
representation, and the overall clarity in depicting system interactions and functionalities. Evaluate the diagram's
ease of interpretation for development, testing, and maintenance, its ability to represent the functionality and
purpose of each class, document object creation instances, and demonstrate the modularity and interface simplicity
that support efficient and reliable system operation.
Faithfulness
• Evaluate how accurately and comprehensively the sequence diagram reflects the system's intended behavior and
requirements specified in the PRD. This includes how well it captures system events, both with and without
parameters, and the accuracy with which it reflects the impact of these events on the system's behavior. Also
Evaluate how accurately and comprehensively the sequence diagram reflects the structural design outlined in the
given UML class diagrams, ensuring a coherent and consistent development process.
```
```
Evaluation Guidance for architecture_design
General Principles
• Uniformity and Integration: The design should demonstrate a consistent style and integrated approach, ensuring all
components work seamlessly together, ensuring high cohesion and decoupling.
• Distinction Between Design and Coding: Recognize that the design process is distinct from coding; good design
lays the groundwork for effective coding but is not synonymous with it.
• Practicability: Evaluate the architecture's practicability by assessing its organization, readability and modularity,
and efficiency. The design should feature a logical and clear structure, evidenced by a well-organized file tree and
distinct class locations in proper directories.
• Conformance: Evaluate the architecture for its conformance to community and industry standards. The file tree
structure, coding practices including naming conventions, documentation and other structural elements should
adhere to the widely accepted conventions by the open-source community and best practices of the programming
language used, such as C/C++, Python, Java and JavaScript.
Faithfulness
• The architecture must be in strict accordance with the given PRD and UML class diagrams. It should accurately
reflect the requirements specified in the PRD and the structural design outlined in the UML diagrams, ensuring a
coherent and consistent development process.
```

Below is the PRD document which is the source of truth for your analysis. 

PRD
-----------
{PRD}


Below are the documents I want you to evaluate:

UML_class
-----------
{UML_class}


UML_sequence
---------------
{UML_sequence}


architecture_design
----------------------
{architecture_design}


Your final response should be a dictionary with keys: 
- "UML_class" : boolean
- "UML_sequence" : boolean
- "architecture_design" : boolean
- "message" : str

The boolean values should represent your judgement on whether the respective document passes or fails the criteria.
The message should provide a brief explanation of your decision and in the event you find errors, provide specific feedback 
on how to correct the mistakes you found.
"""

ENVIRONMENT_SETUP_PROMPT = """

Generate a requirements.txt pip-style to satisfy all the expected dependencies and include unittest as a requirement.
Return a dictionary with key "requirements" and value should be a string that can be written to a file named requirements.txt

Here is the code to consider:
{code}
"""


IMPLEMENTATION_PROMPT = """

Given the files I will pass below, follow the file hierarchy in the "architecture_design" and write each script one-at-a-time. 

Here are the input documents for you to reference:

PRD.md
-----------
{PRD}


UML_class.md
-----------
{UML_class}


UML_sequence.md
---------------
{UML_sequence}


architecture_design.md
----------------------
{architecture_design}


-----Instructions------
Your task is to implement the software based on the PRD and architecture design.
1. Return a dictionary with one key "code" and the value should be another dictionary where:
  - Each key is a full file path as specified in the architecture design
  - Each value is the content of that file
2. Follow the architecture design precisely
3. Include all necessary files from the design, including __init__.py files
4. Keep file paths consistent with this structure throughout your implementation
5. Implement all code files with full, working implementations do not use placeholders such as "TODO" or "pass"
6. Don't specify empty directories
7. Include and generate any CSV/JSON files mentioned in the PRD or architecture design if they are necessary
8. Ensure the code is production-ready and follows best practices 
9. Tests will be run from the root directory of the repository so keep that in mind for import statements
10. Do not import a package that already does the things in the PRD. I want you to generate code that performs the things outlined in the PRD from scratch.
"""

other_imp = """
1. Return a dictionary with a single key "code"
2. The value of "code" should be another dictionary where:
   - Keys: Full file paths as specified in the architecture design
   - Values: Complete, implemented content for each file
3. Ensure all files mentioned in the architecture design are included
4. Be sure to include the following:
   - README.md in the root directory with complete documentation
   - example_usage.sh in the "examples" directory with working examples that are consistent with the PRD
   - if the PRD or architecture design call for other files to be in the "examples" directory then include them as well
5. Implement all code files with full, working implementations
6. Don't specify empty directories
7. Include any CSV/JSON files mentioned in the PRD or architecture design
8. Ensure the code is production-ready and follows best practices 
9. Tests will be run from the root directory of the repository so keep that in mind for import statements
"""

APPROVE_IMPLEMENTATION_PROMPT = """
Review the architectural design and implementation documents below to verify their structural consistency.

Architecture Design:
```
{architecture_design}
```

Implementation Documents:
```
{code}
```

Validation Rules:
- Each file path in the architecture design must have a corresponding implementation file
- Exceptions:
  1. Image-only directories (containing .jpg, .png, etc.)
  2. Empty directories designated for storage
  3. Non-text based files

Response Format:
{{
    "implementation": boolean,  # True if hierarchical mapping is correct
    "message": string  # Detailed analysis and recommendations
}}

Message Guidelines:
- If validation passes: Confirm the correct mapping between design and implementation
- If validation fails:
  1. Identify specific mismatches between architecture_design and documents
  2. Provide clear instructions for necessary corrections
  3. Include a reminder to implement full functionality instead of placeholders (e.g., "TODO" or "pass")

Example Error Message:
"The previous implementation did not correctly map the architecture_design to the documents. Here's how it should be fixed: [specific changes needed]. Remember to provide complete implementations rather than using placeholder code."
"""


OLD_APPROVE_IMPLEMENTATION_PROMPT = """

Below is the architectural design:

```
{architecture_design}
```

Please verify that the architecture design is accurately mirrored in the document list below. Each file path in the architecture design should have a corresponding file in the documents list, with the following exceptions:
- Directories that only contain image files (e.g., .jpg, .png, etc.)
- Empty directories that are intended as storage locations
- Non-text based files since the LLM cannot generate them

```
{code}
```

Your task is to return a dictionary with two keys:
- `"implementation"`: A boolean indicating whether the hierarchical mapping is correct.
- `"message"`: A descriptive confirmation message. If the document names do not agree with the architecture_design
(which is the source of truth) write a prompt saying what the previous implementation did incorrectly and how it should fixed. 
Say something like "The previous implementation did not correctly map the architecture_design to the documents. Here's how it should be fixed: ..."
Also, if there were any issues with the implementation include a reminder not to generate placeholders like "TODO" or "pass" in the code, but to provide full implementations.

Your analysis and response will help ensure consistency and correctness between the architecture_design 
and its representation in code.
"""

ACCEPTANCE_TEST_PROMPT = """
Here are the input documents for you to reference:

PRD.md
-----------
{PRD}

architecture_design.md
----------------------
{architecture_design}

Code
-----------
{code}


--------Instructions--------
Given the inputs, generate appropriate acceptance tests in one file ensuring the software adheres to requirements in the PRD.
Pay close attention to the code and the PRD to ensure the tests are comprehensive and faithful to the PRD.
The acceptance tests will be written using the unittest module and ultimately be written to a file at: tests/acceptance/test_features.py. Keep this in mind.
Write the content of the acceptance test to a dictionary where the key is "test_features" and the value is the content of the acceptance test.
Make another key in this dictionary called "command" and write the command to run the acceptance test as the value for the "command" key.
Nest this dictionary in another dictionary with the key "acceptance_tests" and return this nested dictionary.
"""

UNIT_TEST_PROMPT = """
Here are the input documents for reference:

PRD.md
-----------
{PRD}

architecture_design.md
----------------------
{architecture_design}

Code
-----------
{code}


-----Instructions--------
Your task is to generate unit tests to ensure the software adheres to the requirements in the PRD.

Write the content of the unit tests to a dictionary where the key is "test_module" and the value is the content of the unit tests.
Make another key in this dictionary called "command" and write the command to run the unit test as the value for the "command" key.
Nest this dictionary in another dictionary with the key "unit_tests" and return this nested dictionary as your response.

Requirements:
1. The test_module must contain complete unittest code that tests all functionality
2. Your tests should achieve at least 60 percent coverage
3. Tests will be written to tests/unit/test_module.py - keep this in mind for imports
4. Use the unittest module for all tests
5. Include assertions for both expected and error cases
"""

UNIT_TEST_REVISION_SYSTEM = """
You are a Python unittest expert. Your task is to improve the test coverage of the previous unittest implementation.
"""

UNIT_TEST_REVISION_FEEDBACK = """
The previous tests had insufficient coverage (below 60%). 
Your task is to generate improved tests with better coverage.

To improve coverage, make sure to:
1. Add tests for edge cases (empty inputs, invalid inputs, boundary values)
2. Add tests for error conditions (exceptions, error handling)
3. Test all code paths (different branches, conditional logic)
4. Include more assertions per test case
5. Test both positive and negative scenarios
6. Add tests for any missing functionality

Previous feedback for reference: {feedback}

Remember: 
- Keep using the unittest framework
- Tests will be written to tests/unit/test_module.py
- Make sure your response is a properly formatted dictionary
- Include all necessary imports and test classes in the test_module value

Write the content of the unit tests to a dictionary where the key is "test_module" and the value is the content of the unit tests.
Make another key in this dictionary called "command" and write the command to run the unit test as the value for the "command" key.
Nest this dictionary in another dictionary with the key "unit_tests" and return this nested dictionary as your response.
"""

otherstring = """
-----Instructions--------
Your task is to generate unit tests to ensure the software adheres to the requirements in the PRD.
1. Return a dictionary with one key "unit_tests" and the value should be another dictionary where:
  - The value of the key "test_module" should be the content of the unit test written in the unittest module
  - The value of the key "command" should be the command to run the unit tests
2. Pay close attention to the code and the PRD to ensure the tests are comprehensive and accurate.
3. The unit tests should be written using the unittest module and ultimately written to a file at: tests/unit/test_module.py. Keep this in mind for relative imports and file paths.
"""
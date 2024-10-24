
# we actually want to set these up as structured outputs, but for now we will prompt this way

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
Given the following PRD {PRD}

Return a dictionary with the following keys:
* Create UML class diagram using mermaid syntax as key "UML_class"
* Create  UML sequence diagram using mermaid syntax as key "UML_sequence"
* Create architecture design as a text based representation of the file tree as key "architecture_design"
"""

APPROVE_DESIGN_PROMPT = """
You are a senior software engineer who doesn't miss a thing. 

Review the PRD, UML_class, UML_sequence, and architecture_design under the following Evalution Guidance and Faithfullness criteria 
and judge if they pass or fail. 

Return a dictionary with the following keys "UML_class", "UML_sequence", "architecture_design" and values as boolean.

Evaluation Guidance for UML Class
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


Evaluation Guidance for UML Sequence
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


Evaluation Guidance for Architecture Design
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
"""

REQUIREMENTS_PROMPT = """

Generate a requirements.txt pip-style to satisfy all the expected dependencies and include unittest as a requirement.
Return a dictionary with key "requirements" and value should be a string that can be written to a file named requirements.txt

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
"""


IMPLEMENTATION_PROMPT = """

Given the inputs I will pass below, follow the file hierarchy in the "architecture_design" and write each script one-at-a-time. 

Add each script you generate to the dictionary with the key as the file name and the value as the script content.

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


Requirements.txt
----------------
{requirements}

"""

ACCEPTANCE_TEST_PROMPT = """

Given the inputs, generate appropriate acceptance tests in one file ensuring the software adheres to requirements in the PRD
The acceptance tests must contain the test input (command to execute) and the expected output.

Return a dictionary with key as "acceptance_tests" and value the string that can be written to a python file. 

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


Requirements.txt
----------------
{requirements}

"""

UNIT_TEST_PROMPT = """

Given the inputs I will pass below, generate appropriate unit tests ensuring the software adheres to requirements in the PRD. 

Pay special attention to the UML class diagram and the architecture design.

Return a dictionary with key as "unit_test" and value the string that can be written to a python file.

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


Requirements.txt
----------------
{requirements}

"""





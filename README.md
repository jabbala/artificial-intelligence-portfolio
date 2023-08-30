# Artificial Intelligence Portfolio
Welcome to my AI Portfolio! This portfolio showcases my journey, learnings, and projects in the exciting field of Artificial Intelligence. As a passionate AI enthusiast, I have dedicated time and effort to develop a strong foundation in various AI domains, and this portfolio serves as a testament to my dedication and skills.

## About Me
I am a dedicated and driven individual with a keen interest in AI and its applications. My journey into the world of AI began with a fascination for its potential to transform industries and improve lives. Through self-directed learning, online courses, and hands-on projects, I have cultivated a deep understanding of AI concepts and techniques.

## Portfolio Highlights
### 1. Business Processes Optimization in E-Commerce Warehouse using Q-Learning
Welcome to the Business Processes Optimization in E-Commerce Warehouse project! This repository showcases an AI-driven approach to optimize the operations of an e-commerce warehouse using Q-Learning. By leveraging reinforcement learning techniques, we aim to create an efficient system for managing inventory, order fulfillment, and resource allocation within the warehouse environment.

#### Project Overview
In the fast-paced world of e-commerce, warehouse operations play a crucial role in meeting customer demands. This project focuses on leveraging Q-Learning, a powerful reinforcement learning algorithm, to optimize business processes within an e-commerce warehouse. The Q-Learning agent learns to make decisions that lead to improved inventory management, effective order fulfillment, and optimal resource allocation, ultimately enhancing the overall efficiency of the warehouse.

#### Project Structure
The project is structured as follows:

* `q_learning_agent.py`: Contains the implementation of the Q-Learning agent responsible for making decisions and optimizing warehouse operations.
* `simulation.py`: Simulates the e-commerce warehouse environment, including actions, rewards, and state transitions.
* `main.py`: The main script that orchestrates the optimization process using Q-Learning.
* `utils.py`: Utility functions used throughout the project.

#### Getting Started
Follow these steps to run the project:
* Clone this repository to your local machine.
* Install the required dependencies using pip install -r requirements.txt.
* Configure the simulation parameters, such as the number of states, actions, learning rate, and discount factor, in main.py.
* Run main.py to initiate the Q-Learning optimization process.
* Observe the progress and optimization results in the console output.

#### Results and Evaluation
The project logs the progress of the Q-Learning agent as it optimizes warehouse operations over multiple episodes. You can track the agent's decision-making and the total rewards obtained at each step of the optimization process.

### 2. Minimizing the Costs in Energy Consumption of a Data Center
Welcome to the "Minimizing Energy Costs in Data Center" project! This repository showcases an innovative approach to tackle the challenges of energy consumption in data centers using Deep Q-Learning. By harnessing the power of reinforcement learning, we aim to create an intelligent system that optimizes energy usage, reduces costs, and enhances the sustainability of data center operations.

#### Project Overview
As data centers play a critical role in today's digital landscape, optimizing their energy consumption is paramount. This project focuses on utilizing Deep Q-Learning, a cutting-edge reinforcement learning technique, to minimize energy costs while maintaining the performance and reliability of data center services. By training an AI agent to make energy-efficient decisions, we strive to contribute to both cost savings and environmental conservation.

#### Project Structure
The project is organized as follows:

* `deep_q_learning_agent.py`: Contains the implementation of the Deep Q-Learning agent responsible for making energy consumption decisions.
* `environment.py`: Simulates the data center environment, including actions, rewards, and state transitions related to energy usage.
* `main.py`: The main script that coordinates the optimization process using Deep Q-Learning.
* `utils.py`: Utility functions used throughout the project.

#### Getting Started
Follow these steps to run the project:

* Clone this repository to your local machine.
* Install the required dependencies using `pip install -r requirements.txt`.
* Configure the simulation parameters, neural network architecture, and hyperparameters in `main.py`.
* Run `main.py` to initiate the Deep Q-Learning optimization process.
* Observe the training progress and the agent's decisions through the console output.

#### Results and Evaluation
The project records the agent's progress as it learns to make energy-efficient decisions within the data center environment. You can track the agent's actions, cumulative rewards, and energy consumption over the course of training.

### 3. Self-Driving Car using Deep Q-Learning
In my journey through the realm of Artificial Intelligence, I embarked on an exciting project that brought together the principles of reinforcement learning and autonomous vehicles. This project aimed to develop a self-driving car using Deep Q-Learning, showcasing my proficiency in both AI and real-world applications.

#### Project Overview
The goal of this project was to create an AI agent capable of navigating a virtual environment and driving a car safely while optimizing its path and avoiding obstacles. I chose to implement Deep Q-Learning, a prominent technique in the field of reinforcement learning, to train the agent's decision-making capabilities.

### 4. AI Agent for Doom using Deep Convolutional Q-learning
Diving deeper into the world of AI, I embarked on an exhilarating project that combined the realms of gaming and deep reinforcement learning. The objective of this project was to create an AI agent capable of mastering a complex environment — the DOOM game — using Deep Convolutional Q-Learning. This endeavor not only showcased my technical prowess but also demonstrated my ability to bridge AI methodologies with interactive gaming scenarios.

#### Project Overview
The project's primary goal was to develop an AI agent that could autonomously navigate the challenging landscapes of the DOOM game. Through the implementation of Deep Convolutional Q-Learning, a variant of traditional Q-learning designed to handle high-dimensional state spaces like images, the agent aimed to learn optimal strategies for survival, exploration, and successful mission completion.

### 5. Maximizing Revenue of an Online Retail Business through Thompson Sampling
Welcome to the "Maximizing Revenue of an Online Retail Business" project! This repository presents an innovative approach to optimize the revenue of an online retail business using Thompson Sampling. By leveraging the power of probabilistic algorithms, we aim to create a system that intelligently selects products to promote, maximizing revenue while considering uncertainty and user preferences.

#### Project Overview
In the competitive world of online retail, making informed decisions about which products to promote is crucial for driving revenue. This project focuses on utilizing Thompson Sampling, a Bayesian approach, to address the product selection challenge. By training an AI agent using historical user interactions, we seek to recommend products that have the potential to yield the highest revenue based on user preferences and uncertainty.

#### Project Structure
The project is structured as follows:

* `thompson_sampling_agent.py`: Contains the implementation of the Thompson Sampling agent responsible for selecting products to promote.
* `dataset.py`: Provides a simulated dataset of user interactions with products for training and evaluation.
* `main.py`: The main script that orchestrates the product selection process using Thompson Sampling.
* `utils.py`: Utility functions used throughout the project.

#### Getting Started
Follow these steps to run the project:

* Clone this repository to your local machine.
* Install the required dependencies using pip install -r requirements.txt.
* Configure the parameters related to the simulation, Thompson Sampling algorithm, and user preferences in main.py.
* Run main.py to initiate the product selection process using Thompson Sampling.
* Observe the simulation progress and the agent's selected products through the console output.

#### Results and Evaluation
The project tracks the agent's performance as it learns to choose products that maximize revenue. You can monitor the selected products, their associated rewards, and the overall revenue generated over time.

Keep in mind that this project offers a simplified view of the complexities faced by online retail businesses. Practical implementations would involve real-time data, user behavior modeling, and additional considerations.

### 6. AI Agent for Breakout using Asynchronous Actor-Critic Agents (A3C)
Welcome to the repository showcasing my implementation of the Asynchronous Advantage Actor-Critic (A3C) algorithm to train an AI agent that excels at playing the Breakout game. This project demonstrates the power of parallelism in reinforcement learning by training multiple agents concurrently, ultimately leading to a highly proficient Breakout player.

#### Project Overview
The A3C algorithm is a state-of-the-art method for training deep reinforcement learning agents. It combines the strengths of policy-based and value-based methods, allowing for more stable and efficient learning. In this project, I applied the A3C algorithm to the Breakout game, enabling an AI agent to learn optimal strategies for achieving high scores through trial and error.

## References
* Arthur Juliani, 2016, Simple Reinforcement Learning with Tensorflow (10 Parts)
* Richard Sutton et al., 1998, Reinforcement Learning I: Introduction
* Richard Bellman, 1954, The Theory of Dynamic Programming
* D. J. White, 1993, A Survey of Applications of Markov Decision Processes
* Martijn van Otterlo, 2009, Markov Decision Processes: Concepts and Algorithms
* Richard Sutton, 1988, Learning to Predict by the Methods of Temporal Differences
* Arthur Juliani, 2016, Simple Reinforcement Learning with Tensorflow (Part 4)
* Tom Schaul et al., Google DeepMind, 2016, Prioritized Experience Replay
* Michel Tokic, 2010, Adaptive ε-greedy Exploration in Reinforcement Learning Based on Value Differences
* Richard S. Sutton and Andrew G. Barto, 1998, Reinforcement Learning: An Introduction
* Volodymyr Mnih et al., 2016, Asynchronous Methods for Deep Reinforcement Learning
* Volodymyr Mnih et al, 2016  Asynchronous Methods for Deep Reinforcement Learning
* Jaromír Janisch, 2017 Let’s Make An A3c: Implementation
* John Schulman et al., 2016 High-dimensional Continuous Control Using Generalized Advantage Estimation
* Arthur Juliani, 2016 Simple Reinforcement Learning with Tensorflow (Part 8)

Connect with me on <a href="https://www.linkedin.com/in/jabbala">LinkedIn</a> to discuss this project or other AI endeavors. Let's drive innovation together!

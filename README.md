# Recommender Systems

Recommender systems, or “recommenders” are software systems designed to filter vast volumes and offer personalized recommendations of items or content, based on users' interests and preferences. 
There are several types of recommenders as can be seen in the diagram below:

![Types of recommenders](https://github.com/HeleneRebelo/Recommender-Systems/blob/main/docs/recommender_system.png)

Here we explore:

- **Popularity Rankings or popularity-based**: These are non-personalized recommendations based on popularity rankings, such as best-selling items or most-watched movies. These simplified recommendations may not necessarily reflect quality, as the best-selling item may not be the highest-rated. Additionally, rankings can vary over time, making it important to note recent trends.

- **Memory-based filtering**: This approach is called memory-based because it requires the whole user-item matrix to be retained in the memory of the computer that is providing the recommendations. As we said, this matrix can be huge (humongous!), so this is not a trivial assumption.

     - **User-based**: is a collaborative filtering that analyzes similarities between users' preferences to make recommendations. By comparing their evaluations of items, such as movies, algorithms determine similar user-profiles and suggest items enjoyed by users with similar tastes. This method relies on similarity metrics like cosine similarity or Pearson correlation and recommends items based on patterns of similar users, enabling personalized suggestions for individual users.
     
     - **Item-based**: is a collaborative filtering method that uses similarity between users' preferred and consumed items to make predictions.

## Context

A customer said she wants to put her DVD store online. And you thought all DVD stores were dead! Not quite, WBSFLIX operates in a small town near Berlin and is alive and well thanks to a loyal clientele who appreciate the local atmosphere and, more than anything, the personal recommendations of the owner, Ursula. She is realizing that as her customer base grows, it becomes difficult to find recommendations for each customer.

## Main Objective

1. Develop three recommendation systems based on Popularity, User-based and Item-based.

2. Make these recommenders easily available in a streamlit application that shows film posters, with summary, trailer, and links to [tmdb](https://www.themoviedb.org/) page.

## Challenge

Create recommendation systems that provide WBSFLIX users with relevant content to watch.

## Folder Structure

/docs: This directory contains the final presentation for the project and some images.

/src: Inside this folder, you will find the Notebook with the codes.

### Dataset

The dataset contains around 9742 films. To find out more read: [README.txt](https://github.com/HeleneRebelo/Recommender-Systems/blob/main/data/README.txt)

## Methodology

1. Evaluate the dataset, conduct cleaning, impute missing values, and deal with duplicates to obtain optimal data quality
2. Evaluate which films have the best rating using popularity recommender
3. For the User-based recommender, we used the Surprise library
4. For the item-based recommender, we applied Pearson's correlation and cosine similarity, the second proved to be more robust and we applied it to our model
5. We saved the three resulting recommendation datasets and exported them to our streamlit app which you can see below and in the presentation.

   ![WBSFLIX](https://github.com/HeleneRebelo/Recommender-Systems/blob/main/docs/wbsflix_image.png)

### This project was made possible by the collaborative efforts of our team:
Me, Dante Lertora and [Sweta Bhattarai](https://github.com/SwetaBhattarai)
   





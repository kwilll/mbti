Preprocessing

    1. Import Data using pandas
    2. Count frequency of MBTI types in the data
    3. Eliminate extra rows to represent actual population
    4. Convert urls to "URL"
    5. Remove punctuation
    4. Make all text posts lower case
    6. Selective Word Removal
    7. Stop Word Removal
    8. Lemmatization
    9. Tokenization
    10. Padding 
    11. Create word clouds for MBTI types

Model

    1. Create embedding layer matrix mapping to 50 dimensionsl matrix GloVe representation
    
    2. RNN - turn equations into code
        Recommended Parameters (can be modified to fine tune):
            LSTM layer dropout 0.1
            recurrent dropout 0.1
            sigmoid activation
            zero kernel initializer
    
    3. Dense Layer
        sigmoid activation to produce value between 0 and 1, representing predicted class probability
    
    4. (Other
        binary crossentropy for loss function and Adam optimizer)
        
Experiments
    
    Data set
        each row 2 columns, [mbti, 50 posts]
        split data into training data and testing data: 75/25
        data points = # of rows * # of MBTI types
            for full data set = 433,750 data points
            cleaned data set = 31,200 data points (16 types * 39 rows/type * 50 posts/row)
    
    Classification Task
        break 16 classes into 4 binary classification tasks

    Training Configurations
        
        Model batch size: 624 (468 for training, 156 for testing)
        Token vocab size: 2500
        Input vector length: 40
        Embeddint vector length: 50
        number of epochs: (30)

    Evaluation

        Post Classification Methodology
            Use test data to produce accuracy score and confusion matrix for every MBTI dimension

        User Classification Methodology
            take the mean of the class probability predictions for al the posts ni a user's corpus and round either to 0 or 1

Results

    Post Classification
        Accuracy
        Confusion matrices for each binary choice (4)
    
    User Classification
        Accuracy
        Confusion matrices (4)

Analysis

    Model efficacy and Implications

    Word Clouds (16 split into 4x2 for each binary)

    Generalizability to Social Media
        Try it in real life

Conclusion

References

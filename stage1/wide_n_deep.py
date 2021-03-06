# coding: utf-8
# pylint: disable=C0103, C0111

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import pandas as pd
import tensorflow as tf
import tensorflow.contrib.layers as layers
import tensorflow.contrib.learn as learn
import tempfile
import datetime

from feature import get_tf_feature, split_train_test

tf.logging.set_verbosity(
    tf.logging.INFO)  # Set to INFO for tracking training, default is WARN. ERROR for least messages

COLUMNS_DICT = {
    'category': [
        'userID',
        'creativeID',
        'positionID',
        'adID',
        'camgaignID',
        'advertiserID',
        'appID',
        'sitesetID',
        'connectionType',
        'telecomsOperator',
        'appPlatform',
        'appCategory',
        'gender',
        'education',
        'marriageStatus',
        'haveBaby',
        'hometown_p',
        'hometown_c',
        'residence_p',
        'residence_c',
        'positionType',
        'clickTime_week'
    ],
    'continue': [
        'age', 'inst_cnt_appcate', 'inst_cnt_installed', 'inst_cate_percent',
        'inst_is_installed', 'inst_app_installed', 'action_installed',
        'action_cate', 'action_cate_recent', 'tt_is_installed',
        'tt_cnt_appcate', 'clickTime_day', 'clickTime_hour', 'clickTime_minute'
    ]
}

COLUMNS = COLUMNS_DICT['category'] + COLUMNS_DICT['continue']

LABEL_COLUMN = ["label"]
CATEGORICAL_COLUMNS = COLUMNS_DICT['category']
CONTINUOUS_COLUMNS = COLUMNS_DICT['continue']

G_COLUMNS = []
BATCH_SIZE = 40
RECORD = []


def build_estimator(model_dir, model_type):
    """Build an estimator."""
    # Sparse base columns.
    userID = layers.sparse_column_with_integerized_feature('userID', 2805118)
    creativeID = layers.sparse_column_with_integerized_feature('creativeID', 6582)
    positionID = layers.sparse_column_with_integerized_feature('positionID', 7645)
    adID = layers.sparse_column_with_integerized_feature('adID', 3616)
    camgaignID = layers.sparse_column_with_integerized_feature('camgaignID', 720)
    advertiserID = layers.sparse_column_with_integerized_feature('advertiserID', 91)
    appID = layers.sparse_column_with_integerized_feature('appID', 50)
    sitesetID = layers.sparse_column_with_integerized_feature('sitesetID', 3)
    appCategory = layers.sparse_column_with_integerized_feature('appCategory', 14)
    appPlatform = layers.sparse_column_with_integerized_feature('appPlatform', 2)
    education = layers.sparse_column_with_integerized_feature('education', 8)
    gender = layers.sparse_column_with_integerized_feature('gender', 3)
    haveBaby = layers.sparse_column_with_integerized_feature('haveBaby', 7)
    marriageStatus = layers.sparse_column_with_integerized_feature('marriageStatus', 4)
    positionType = layers.sparse_column_with_integerized_feature('positionType', 6)
    hometown_c = layers.sparse_column_with_integerized_feature('hometown_c', 22)
    hometown_p = layers.sparse_column_with_integerized_feature('hometown_p', 35)
    residence_c = layers.sparse_column_with_integerized_feature('residence_c', 22)
    residence_p = layers.sparse_column_with_integerized_feature('residence_p', 35)
    telecomsOperator = layers.sparse_column_with_integerized_feature('telecomsOperator', 4)
    connectionType = layers.sparse_column_with_integerized_feature('connectionType', 5)
    clickTime_week = layers.sparse_column_with_integerized_feature('clickTime_week', 7)

    # Continuous base columns.
    age = layers.real_valued_column("age")
    inst_app_installed = layers.real_valued_column('inst_app_installed')
    inst_cate_percent = layers.real_valued_column('inst_cate_percent')
    inst_cnt_appcate = layers.real_valued_column('inst_cnt_appcate')
    inst_cnt_installed = layers.real_valued_column('inst_cnt_installed')
    inst_is_installed = layers.real_valued_column('inst_is_installed')
    action_cate = layers.real_valued_column('action_cate')
    action_cate_recent = layers.real_valued_column('action_cate_recent')
    action_installed = layers.real_valued_column('action_installed')
    tt_cnt_appcate = layers.real_valued_column('tt_cnt_appcate')
    tt_is_installed = layers.real_valued_column('tt_is_installed')
    clickTime_day = layers.real_valued_column('clickTime_day')
    clickTime_hour = layers.real_valued_column('clickTime_hour')
    clickTime_minute = layers.real_valued_column('clickTime_minute')

    # Transformations.
    age_buckets = layers.bucketized_column(
        age, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])
    inst_app_installed_buckets = layers.bucketized_column(
        inst_app_installed,
        boundaries=[1000, 5000, 10000, 50000, 100000, 500000])
    clickTime_hour_buckets = layers.bucketized_column(
        clickTime_hour, boundaries=[8, 11, 14, 17, 19, 22])

    # Wide columns and deep columns.
    wide_columns = [
        userID,
        creativeID,
        positionID,
        adID,
        camgaignID,
        advertiserID,
        appID,
        sitesetID,
        appCategory,
        appPlatform,
        education,
        gender,
        haveBaby,
        marriageStatus,
        positionType,
        hometown_c,
        hometown_p,
        residence_c,
        residence_p,
        telecomsOperator,
        connectionType,
        clickTime_week,

        # layers.embedding_column(userID, dimension=8),
        # layers.embedding_column(creativeID, dimension=8),
        # layers.embedding_column(positionID, dimension=8),
        # layers.embedding_column(adID, dimension=8),
        # layers.embedding_column(camgaignID, dimension=8),
        # layers.embedding_column(advertiserID, dimension=8),
        # layers.embedding_column(appID, dimension=8),
        # layers.embedding_column(sitesetID, dimension=8),
        # layers.embedding_column(appCategory, dimension=8),
        # layers.embedding_column(appPlatform, dimension=8),
        # layers.embedding_column(education, dimension=8),
        # layers.embedding_column(gender, dimension=8),
        # layers.embedding_column(haveBaby, dimension=8),
        # layers.embedding_column(marriageStatus, dimension=8),
        # layers.embedding_column(positionType, dimension=8),
        # layers.embedding_column(hometown_c, dimension=8),
        # layers.embedding_column(hometown_p, dimension=8),
        # layers.embedding_column(residence_c, dimension=8),
        # layers.embedding_column(residence_p, dimension=8),
        # layers.embedding_column(telecomsOperator, dimension=8),
        # layers.embedding_column(connectionType, dimension=8),
        # layers.embedding_column(clickTime_week, dimension=8),
        # layers.one_hot_column(userID),
        # layers.one_hot_column(creativeID),
        # layers.one_hot_column(positionID),
        # layers.one_hot_column(adID),
        # layers.one_hot_column(camgaignID),
        # layers.one_hot_column(advertiserID),
        # layers.one_hot_column(appID),
        # layers.one_hot_column(sitesetID),
        # layers.one_hot_column(appCategory),
        # layers.one_hot_column(appPlatform),
        # layers.one_hot_column(education),
        # layers.one_hot_column(gender),
        # layers.one_hot_column(haveBaby),
        # layers.one_hot_column(marriageStatus),
        # layers.one_hot_column(positionType),
        # layers.one_hot_column(hometown_c),
        # layers.one_hot_column(hometown_p),
        # layers.one_hot_column(residence_c),
        # layers.one_hot_column(residence_p),
        # layers.one_hot_column(telecomsOperator),
        # layers.one_hot_column(connectionType),
        # layers.one_hot_column(clickTime_week),
        age_buckets,
        clickTime_hour_buckets,
        inst_app_installed_buckets,
    ]

    deep_columns = [
        layers.embedding_column(userID, dimension=8),
        layers.embedding_column(creativeID, dimension=8),
        layers.embedding_column(positionID, dimension=8),
        layers.embedding_column(adID, dimension=8),
        layers.embedding_column(camgaignID, dimension=8),
        layers.embedding_column(advertiserID, dimension=8),
        layers.embedding_column(appID, dimension=8),
        layers.embedding_column(sitesetID, dimension=8),
        layers.embedding_column(appCategory, dimension=8),
        layers.embedding_column(appPlatform, dimension=8),
        layers.embedding_column(education, dimension=8),
        layers.embedding_column(gender, dimension=8),
        layers.embedding_column(haveBaby, dimension=8),
        layers.embedding_column(marriageStatus, dimension=8),
        layers.embedding_column(positionType, dimension=8),
        layers.embedding_column(hometown_c, dimension=8),
        layers.embedding_column(hometown_p, dimension=8),
        layers.embedding_column(residence_c, dimension=8),
        layers.embedding_column(residence_p, dimension=8),
        layers.embedding_column(telecomsOperator, dimension=8),
        layers.embedding_column(connectionType, dimension=8),
        layers.embedding_column(clickTime_week, dimension=8),
        age,
        action_cate,
        action_cate_recent,
        action_installed,
        inst_app_installed,
        inst_cate_percent,
        inst_cnt_appcate,
        inst_cnt_installed,
        inst_is_installed,
        tt_cnt_appcate,
        tt_is_installed,
        clickTime_day,
        clickTime_hour,
        clickTime_minute,
    ]

    if model_type == "wide":
        m = tf.contrib.learn.LinearClassifier(
            model_dir=model_dir, feature_columns=wide_columns)
    elif model_type == "deep":
        m = tf.contrib.learn.DNNClassifier(
            model_dir=model_dir,
            feature_columns=deep_columns,
            hidden_units=[100, 50])
    else:
        m = tf.contrib.learn.DNNLinearCombinedClassifier(
            model_dir=model_dir,
            linear_feature_columns=wide_columns,
            dnn_feature_columns=deep_columns,
            dnn_hidden_units=[100, 50, 1],
            fix_global_step_increment_bug=True)
    return m


def input_fn(filename, columns=G_COLUMNS, batch_size=BATCH_SIZE, record=RECORD):
    """Input builder function."""
    # Creates a dictionary mapping from each continuous feature column name (k) to
    # the values of that column stored in a constant Tensor.
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TextLineReader()
    key, value = reader.read_up_to(filename_queue, num_records=batch_size)
    record_defaults = []
    for c in columns:
        if c in CATEGORICAL_COLUMNS:
            record_defaults.append([0])
        else:
            record_defaults.append([0.0])

    data = tf.decode_csv(value, record_defaults=record_defaults)

    # features is a dictionary that maps from column names to tensors of the data.
    # income_bracket is the last column of the data. Note that this is NOT a dict.
    all_columns = dict(zip(G_COLUMNS, data))

    # Save the label column
    # dict.pop() returns the popped array of label values
    labels = all_columns.pop(LABEL_COLUMN[0])

    # the remaining columns are our features
    features = all_columns

    # Sparse categorical features must be represented with an additional dimension.
    # There is no additional work needed for the Continuous columns; they are the unaltered columns.
    # See docs for tf.SparseTensor for more info
    for feature_name in CATEGORICAL_COLUMNS:
        features[feature_name] = tf.expand_dims(features[feature_name], -1)

    return features, labels


def train_and_eval(df_train, df_val, df_test, columns, train_steps):
    """Train and evaluate the model."""
    # remove NaN elements
    # df_train = df_train.dropna(how='any', axis=0)
    # df_val = df_val.dropna(how='any', axis=0)

    model_dir = tempfile.mkdtemp()
    print("model directory = %s" % model_dir)

    m = build_estimator(model_dir, 'wide-n-deep')
    m.fit(input_fn=lambda: input_fn(df_train, columns=columns), steps=train_steps)
    results = m.evaluate(
        input_fn=lambda: input_fn(df_val, columns=columns), steps=1, matrices=['logloss'])
    for key in sorted(results):
        print("%s: %s" % (key, results[key]))

    x, _ = input_fn(df_test.drop(['instanceID'], axis=1))

    pred_x = m.predict(x)
    result = pd.DataFrame(df_test['instanceID'])
    result['prob'] = list(pred_x)
    result.to_csv("submission.{}.csv".format(datetime.datetime.now()), index=False)


FLAGS = None


def to_int(df):
    for c in CATEGORICAL_COLUMNS:
        df[c] = df[c].astype(int)

    return df


def main(_):
    df_train, df_test = get_tf_feature(with_ohe=False, save=True, needDF=True)
    df_train, df_val = split_train_test(df_train, None, with_df=True)

    # conver to int
    df_train = to_int(df_train)
    df_val = to_int(df_val)
    df_test = to_int(df_test)

    # save data for queue to read
    df_train.to_csv('wd_df_train.csv', index=False, header=False)
    df_val.to_csv('wd_df_val.csv', index=False, header=False)
    df_test.to_csv('wd_df_test.csv', index=False, header=False)

    # RECORD = df_train.iloc[0, :]

    train_and_eval('wd_df_train.csv', 'wd_df_val.csv', df_test, df_train.columns, train_steps=200)


if __name__ == "__main__":
    tf.app.run(main=main)

# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines constants for interpret community."""

from enum import Enum


class ExplanationParams(object):
    """Provide constants for explanation parameters."""

    EXPECTED_VALUES = 'expected_values'
    CLASSES = 'classes'


class ExplainType(object):
    """Provide constants for model and explainer type information, useful for visualization."""

    CLASSIFICATION = 'classification'
    DATA = 'data_type'
    EXPLAIN = 'explain_type'
    EXPLAINER = 'explainer'
    FUNCTION = 'function'
    HAN = 'han'
    IS_RAW = 'is_raw'
    LIME = 'lime'
    METHOD = 'method'
    MIMIC = 'mimic'
    MODEL = 'model_type'
    MODEL_CLASS = 'model_class'
    MODEL_TASK = 'model_task'
    PFI = 'pfi'
    REGRESSION = 'regression'
    SHAP = 'shap'
    SHAP_DEEP = 'shap_deep'
    SHAP_KERNEL = 'shap_kernel'
    SHAP_TREE = 'shap_tree'
    SHAP_LINEAR = 'shap_linear'
    TABULAR = 'tabular'


class ExplainParams(object):
    """Provide constants for interpret community (init, explain_local and explain_global) parameters."""

    BATCH_SIZE = 'batch_size'
    CLASSES = 'classes'
    CLASSIFICATION = 'classification'
    EVAL_DATA = 'eval_data'
    EVAL_Y_PRED = 'eval_y_predicted'
    EVAL_Y_PRED_PROBA = 'eval_y_predicted_proba'
    EXPECTED_VALUES = 'expected_values'
    EXPLAIN_SUBSET = 'explain_subset'
    EXPLANATION_ID = 'explanation_id'
    FEATURES = 'features'
    GLOBAL_IMPORTANCE_NAMES = 'global_importance_names'
    GLOBAL_IMPORTANCE_VALUES = 'global_importance_values'
    GLOBAL_IMPORTANCE_RANK = 'global_importance_rank'
    ID = 'id'
    INCLUDE_LOCAL = 'include_local'
    INIT_DATA = 'init_data'
    IS_RAW = 'is_raw'
    LOCAL_EXPLANATION = 'local_explanation'
    LOCAL_IMPORTANCE_VALUES = 'local_importance_values'
    METHOD = 'method'
    MODEL_ID = 'model_id'
    MODEL_TASK = 'model_task'
    MODEL_TYPE = 'model_type'
    PER_CLASS_NAMES = 'per_class_names'
    PER_CLASS_RANK = 'per_class_rank'
    PER_CLASS_VALUES = 'per_class_values'
    PROBABILITIES = 'probabilities'
    SAMPLING_POLICY = 'sampling_policy'
    SHAP_VALUES_OUTPUT = 'shap_values_output'

    @classmethod
    def get_serializable(cls):
        """Return only the ExplainParams properties that have meaningful data values for serialization.

        :return: set of property names - e.g. 'GLOBAL_IMPORTANCE_VALUES', 'MODEL_TYPE', etc.
        :rtype: set{str}
        """
        return (set(filter(lambda x: not x.startswith('__') and not callable(getattr(cls, x)),
                vars(cls).keys())) - set(['DATA_MAPPER', 'DATA_MAPPER_INTERNAL']))


class Defaults(object):
    """Provide constants for default values to explain methods."""

    AUTO = 'auto'
    DEFAULT_BATCH_SIZE = 100
    # hdbscan is an unsupervised learning library to find the optimal number of clusters in a dataset
    # See this github repo for more details: https://github.com/scikit-learn-contrib/hdbscan
    HDBSCAN = 'hdbscan'
    MAX_DIM = 50


class Attributes(object):
    """Provide constants for attributes."""

    EXPECTED_VALUE = 'expected_value'


class Dynamic(object):
    """Provide constants for dynamically generated classes."""

    GLOBAL_EXPLANATION = 'DynamicGlobalExplanation'
    LOCAL_EXPLANATION = 'DynamicLocalExplanation'


class Tensorflow(object):
    """Provide TensorFlow and Tensorboard related constants."""

    CPU0 = '/CPU:0'
    TFLOG = 'tflog'


class SKLearn(object):
    """Provide scikit-learn related constants."""

    EXAMPLES = 'examples'
    LABELS = 'labels'
    PREDICTIONS = 'predictions'


class Spacy(object):
    """Provide spacy related constants."""

    EN = 'en'
    NER = 'ner'
    TAGGER = 'tagger'


class ModelTask(str, Enum):
    """Provide model task constants.  Can be classification, regression or unknown.

    By default we infer the model domain if Unknown, but this can be overridden by the user if they
    specify classification or regression.
    """

    Classification = 'classification'
    Regression = 'regression'
    Unknown = 'unknown'


class LightGBMParams(object):
    """Provide constants for LightGBM."""

    CATEGORICAL_FEATURE = 'categorical_feature'


class ShapValuesOutput(str, Enum):
    """Provide constants for the shap values output from the explainer.

    Can be default, probability or teacher_probability. If teacher probability is specified,
    we use the probabilities from the teacher model.
    """

    DEFAULT = 'default'
    PROBABILITY = 'probability'
    TEACHER_PROBABILITY = 'teacher_probability'


class ExplainableModelType(str, Enum):
    """Provide constants for the explainable model type."""

    TREE_EXPLAINABLE_MODEL_TYPE = 'tree_explainable_model_type'
    LINEAR_EXPLAINABLE_MODEL_TYPE = 'linear_explainable_model_type'


class MimicSerializationConstants(object):
    """Provide internal class that defines fields used for MimicExplainer serialization."""

    FUNCTION = 'function'
    IDENTITY = '_identity'
    INITIALIZATION_EXAMPLES = 'initialization_examples'
    LOGGER = '_logger'
    MODEL = 'model'
    ORIGINAL_EVAL_EXAMPLES = '_original_eval_examples'
    PREDICT_PROBA_FLAG = 'predict_proba_flag'

    enum_properties = ['_shap_values_output']
    nonify_properties = ['_logger', 'model', 'function', 'initialization_examples', '_original_eval_examples']
    save_properties = ['surrogate_model']


class LightGBMSerializationConstants(object):
    """Provide internal class that defines fields used for MimicExplainer serialization."""

    IDENTITY = '_identity'
    LOGGER = '_logger'
    MODEL_STR = 'model_str'
    MULTICLASS = 'multiclass'
    TREE_EXPLAINER = '_tree_explainer'
    OBJECTIVE = 'objective'

    enum_properties = ['_shap_values_output']
    nonify_properties = [LOGGER, TREE_EXPLAINER]
    save_properties = ['_lgbm']


class DNNFramework(object):
    """Provide DNN framework constants."""

    TENSORFLOW = 'tensorflow'
    PYTORCH = 'pytorch'


class InterpretData(object):
    """Provide Data and Visualize constants for interpret core."""

    BASE_VALUE = 'Base Value'
    EXPLANATION_TYPE = 'explanation_type'
    EXTRA = 'extra'
    FEATURE_LIST = 'feature_list'
    GLOBAL_FEATURE_IMPORTANCE = 'global_feature_importance'
    INTERCEPT = 'intercept'
    LOCAL_FEATURE_IMPORTANCE = 'local_feature_importance'
    MLI = 'mli'
    NAMES = 'names'
    OVERALL = 'overall'
    PERF = 'perf'
    SCORES = 'scores'
    SPECIFIC = 'specific'
    TYPE = 'type'
    UNIVARIATE = 'univariate'
    VALUE = 'value'
    VALUES = 'values'


class Extension(object):
    """Provide constants for extensions to interpret package."""

    BLACKBOX = 'blackbox'
    GLASSBOX = 'model'
    GLOBAL = 'global'
    GREYBOX = 'specific'
    LOCAL = 'local'

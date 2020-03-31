PROBLEM = 'score2perf_maestro_language_uncropped_aug'

from tensor2tensor import problems

TMP_DIR = 'tmp/' # Where data files from internet stored
DATA_DIR = 'dataset/' # Where pre-prcessed data is stored

# # Init problem T2T object the generated training data
t2t_problem = problems.problem(PROBLEM)
t2t_problem.generate_data(DATA_DIR, TMP_DIR) 


# # # Init Hparams object from T2T Problem
# hparams = trainer_lib.create_hparams(HPARAMS)
# hp = json.loads(hparams.to_json())
# # hparams.batch_size = 5
# # hparams.batch_shuffle_size = 1
# hparams.num_hidden_layers = 6
# hparams.hidden_size = 256
# # hparams.max_length = 2048
# hparams.filter_size = 2048
# hparams.num_heads = 8
# hparams.batch_size = 128

# # below comes from score2perf hparams setting
# hparams.shared_embedding_and_softmax_weights = False
# hparams.symbol_modality_num_shards = 1
# hparams.label_smoothing = 0.0

# hparams.layer_prepostprocess_dropout = 0.1
# hparams.attention_dropout = 0.1
# hparams.relu_dropout = 0.1

# hparams.max_length = 0
# hparams.batch_size = 2048

# hparams.sampling_method = "random"
# hparams.summarize_vars = True


# # hparams.self_attention_type = "dot_product_relative_v2"

# hp = json.loads(hparams.to_json())
# print(hp, "hparams")

# # Initi Run Config for Model Training
# RUN_CONFIG = trainer_lib.create_run_config(
#       model_dir=TRAIN_DIR,
#     #   model_name=MODEL,
#       save_checkpoints_steps=2000
# )
# print("Create experiment....")

# # # Create Tensorflow Experiment Object
# tensorflow_exp_fn = trainer_lib.create_experiment(
#         run_config=RUN_CONFIG,
#         hparams=hparams,
#         model_name=MODEL,
#         problem_name=PROBLEM,
#         data_dir=DATA_DIR, 
#         train_steps=1500 * 1000, # Total number of train steps for all Epochs
#         eval_steps=100
#     )

# # # Kick off Training
# print("Start training....")
# tensorflow_exp_fn.train_and_evaluate()
# tensorflow_exp_fn.train_eval_and_decode()
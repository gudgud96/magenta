PROBLEM=score2perf_maestro_language_uncropped_aug

PIPELINE_OPTIONS=\
"--runner=DataflowRunner,"\
"--temp_location=tmp,"\
"--setup_file=/path/to/setup.py"

t2t-datagen \
  --data_dir=dataset \
  --problem=${PROBLEM} \
  --pipeline_options="${PIPELINE_OPTIONS}" \
  --alsologtostderr
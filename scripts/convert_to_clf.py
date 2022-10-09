import sys

from clickspoil.util.io import read_jsonl, write_jsonl

input_file = sys.argv[1]
output_file = sys.argv[2]

records = read_jsonl(input_file)

labels = ["phrase", "passage", "multi"]
clf_records = []
for record in records:
    label_idx = None
    if "tags" in record:
        label = record["tags"][0]
        assert label in labels
        label_idx = labels.index(label)
    clf_record = {
        "uuid": record["uuid"],
        "post_text": record["postText"][0]
    }

    context = []
    if "targetTitle" in record:
        context.append(record["targetTitle"])
    if "targetParagraphs" in record:
        context.extend(record["targetParagraphs"])
    if context:
        clf_record["context"] = context
    if label_idx:
        clf_record["label"] = label_idx
    clf_records.append(clf_record)

write_jsonl(clf_records, output_file)


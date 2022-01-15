import sacrebleu

sys = ['Code doctor studio is good at various AI algorithms']
sysorg = ['Code doctor studio engaged in AI algorithms related work']
refs = [['Code doctor studio engaged in AI algorithms related work']]
print(sacrebleu.corpus_bleu(sys, refs).score)
print(sacrebleu.corpus_bleu(sysorg, refs).score)
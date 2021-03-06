# Temporal and Aspectual Entailment - Resources #

This repository contains the datasets used in our [IWCS 2019 paper](https://github.com/tttthomasssss/iwcs2019/blob/master/TemporalAndAspectualEntailment.pdf) _Temporal and Aspectual Entailment_. If you use any of the resources in your own work, please use the following bibtex entry:

```

@inproceedings{Kober_2019,
	Address = {Gothenburg, Sweden},
	Author = {Kober, Thomas and de Vroe, Sander Bijl and Steedman, Mark},
	Booktitle = {Proceedings of the 13th International Conference on Computational Semantics - Long Papers},
	Month = {23{--}27 } # may,
	Pages = {103--119},
	Publisher = {Association for Computational Linguistics},
	Title = {Temporal and Aspectual Entailment},
	Year = {2019}}
```

### Datasets ###

All datasets are in the [datasets](https://github.com/tttthomasssss/iwcs2019/tree/master/datasets) folder of this repository.

#### Auxiliary-Verb Agreement ####

The [dataset](https://github.com/tttthomasssss/iwcs2019/blob/master/datasets/aux_verb_agreement.txt) is tab separated and contains correct (e.g. _will visit_) and incorrect (e.g. _will visiting_) auxiliary-verb phrases together with their classification labels (`1=correct; 0=incorrect`). The goal is to detect whether agreement information is encoded in the representations and can be detected with a linear classifier. In our paper we used a Logistic Regression classifier from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn-linear-model-logisticregression) with default hyperparameter settings (the solver was set to `liblinear`). See our [paper]((https://github.com/tttthomasssss/iwcs2019/blob/master/TemporalAndAspectualEntailment.pdf)) for further details.

#### Translation Operation ####

The [dataset](https://github.com/tttthomasssss/iwcs2019/blob/master/datasets/translation_operation.txt) is tab separated and contains the auxiliary, the corresponding inflected verb and the infinitive form of a verb. The goal is to learn a translation operation from infinitive forms to inflected forms (or contextualised forms if the tense uses auxiliaries). Evaluation has been done using Mean Reciprocal Rank (MRR) - see our [paper]((https://github.com/tttthomasssss/iwcs2019/blob/master/TemporalAndAspectualEntailment.pdf)) for further details.

The code for our feedforward network that generates an inflected verb given its infinitive is in [code](https://github.com/tttthomasssss/iwcs2019/tree/master/code). It requires `torch>=1.0.0`, however its a very vanilla feedforward network and should be easily reproducible (haha, famous last words!) in any other framework too.

#### Temporal Entailment Assessment (TEA) ####

**[TEA](https://github.com/tttthomasssss/iwcs2019/blob/master/datasets/TEA.txt)** is an entailment dataset in our [paper]((https://github.com/tttthomasssss/iwcs2019/blob/master/TemporalAndAspectualEntailment.pdf)) and contains 11138 sentence pairs. The labels specify whether sentence 1 entails sentence 2. **[TEA](https://github.com/tttthomasssss/iwcs2019/blob/master/datasets/TEA.txt)** follows a very simple structure and differs only in tense and aspect of the main verb (and potentially in a preposition or particle in order to make the sentence felicitous). The dataset furthermore contains information about the tense and aspect of the sentences. The label coding is `1=entailment` and `0=no entailment`. For the pre-trained SNLI experiment we mapped `contradiction` and `neutral` predictions to `no entailment` in the evaluation.  See our [paper]((https://github.com/tttthomasssss/iwcs2019/blob/master/TemporalAndAspectualEntailment.pdf)) (and its Appendix) for further details.

Because consistency is boring, **[TEA](https://github.com/tttthomasssss/iwcs2019/blob/master/datasets/TEA.txt)** is comma separated rather than tab separated.
r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers


def part1_rnn_hyperparams():
    hypers = dict(
        batch_size=0,
        seq_len=0,
        h_dim=0,
        n_layers=0,
        dropout=0,
        learn_rate=0.0,
        lr_sched_factor=0.0,
        lr_sched_patience=0,
    )
    # TODO: Set the hyperparameters to train the model.
    # ====== YOUR CODE: ======
    hypers['batch_size'] = 256
    hypers['seq_len'] = 64
    hypers['h_dim'] = 512
    hypers['n_layers'] = 3
    hypers['dropout'] = 0.5
    hypers['learn_rate'] = 0.001
    hypers['lr_sched_factor'] = 0.5
    hypers['lr_sched_patience'] = 2
    # ========================
    return hypers


def part1_generation_params():
    start_seq = ""
    temperature = 0.0001
    # TODO: Tweak the parameters to generate a literary masterpiece.
    # ====== YOUR CODE: ======
    start_seq = "ALLS WELL THAT ENDS WELL"
    # ========================
    return start_seq, temperature


part1_q1 = r"""
We split the corpus into sequences due to the following reasons:
1.  Not exhausting our memory resources: for each char in the corpus we create a one hot vector in a length of all 
    chars in the corpus. Not splitting the corpus into sequences will result in a huge matrix that might not fit the
    entire memory.
2.  Splitting the whole corpus into sequences makes the batches data-independent in a some sense, and adds a layer of 
    "creativity" to the training process. Thus preventing the model overfit the corpus itself
"""

part1_q2 = r"""
The generated text shows memory longer than the sequence length because the output of every epoch is not only dependant
on the input, but also on the hidden state which is a result of the previous stages thus it acts as our memory in a way.
"""

part1_q3 = r"""
We are not shuffling the order of batches when training, because despite previous models that we learnt on, where the
order of the samples wasn't important at all. For new chars the RNN needs to be able to learn from the previous ones, 
and to be able to see the logical connection between them, in order to create the correct patterns. Thus shuffeling 
the order will interfere the training process and will result in creating the wrong patterns.

"""

part1_q4 = r"""
**Your answer:**
1.  The temperature, as explained in the excersise is a hyper parameter that controls the variance of the distribution
for the next char in conditioned on the current one and the current state of the model. Low temperature value leads to 
a lower variance, thus resulting in maximising the chances of choosing the correct answer. In another words it maximising
the chances of our model to over fit the training data.  
When sampling we would like to choose lower temperature, since in that stage, and assuming our model is well trained, 
we do want the model to generate the answer it thinks most fit.

2.  Choosing higher values of temperature will lead to higher variance of the next char distribution, which means higher
chances for choosing random chars, resulting in more made up words and more spelling mistakes. The model will be more
"creative" in a way.

3.  Choosing lower values of temperature will lead to lower variance of the next char distribution, which means 
more confidence in choosing character which results in better spelling, however in less diversity in the generated text.
The model will be more "conservative" in a way.
"""
# ==============


# ==============
# Part 2 answers

PART2_CUSTOM_DATA_URL = None


def part2_vae_hyperparams():
    hypers = dict(
        batch_size=0, h_dim=0, z_dim=0, x_sigma2=0, learn_rate=0.0, betas=(0.0, 0.0),
    )
    # TODO: Tweak the hyperparameters to generate a former president.
    # ====== YOUR CODE: ======
    hypers['batch_size'] = 8
    hypers['h_dim'] = 512
    hypers['z_dim'] = 256
    hypers['x_sigma2'] = 0.001
    hypers['learn_rate'] = 1e-4
    hypers['betas'] = (0.9, 0.99)
    # ========================
    return hypers


part2_q1 = r"""
Sigma hyperparameter controls the influence of the data loss. It serves the model as a fine tunning to
how far from the mean can the model go.

On lower values of sigma - the model will generate new data the is close to the inputs.
On higher values of sigma - the model will be more flexible and creative, so that the new data will different than
the inputs in comparison to the data generated by lower values of sigma.
"""

part2_q2 = r"""
1.  The purpose of the reconstruction term in the loss function is to measure how well our decoder can reconstruct an image.
    This measurement helps our model in the training process so we can increase accuracy to generate an image that
    resembles the original inputs.
    
    The purpose of the KL divergence term in the loss function is to make the distribution of the encoder output
    as close as possible to a standard multivariate normal distribution.
    
2.  
"""

part2_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q4 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

PART3_CUSTOM_DATA_URL = None


def part3_gan_hyperparams():
    hypers = dict(
        batch_size=0,
        z_dim=0,
        data_label=0,
        label_noise=0.0,
        discriminator_optimizer=dict(
            type="",  # Any name in nn.optim like SGD, Adam
            lr=0.0,
            # You an add extra args for the optimizer here
        ),
        generator_optimizer=dict(
            type="",  # Any name in nn.optim like SGD, Adam
            lr=0.0,
            # You an add extra args for the optimizer here
        ),
    )
    # TODO: Tweak the hyperparameters to train your GAN.
    # ====== YOUR CODE: ======
    hypers['batch_size'] = 32
    hypers['z_dim'] = 4
    hypers['label_noise'] = 0.2
    hypers['data_label'] = 1
    hypers['discriminator_optimizer']['type'] = 'Adam'
    hypers['discriminator_optimizer']['lr'] = 0.0002
    hypers['discriminator_optimizer']['betas'] = (0.5, 0.99)
    hypers['generator_optimizer']['type'] = 'Adam'
    hypers['generator_optimizer']['lr'] = 0.0002
    hypers['generator_optimizer']['betas'] = (0.5, 0.99)
    # ========================
    return hypers


part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

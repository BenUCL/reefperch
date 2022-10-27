# coding=utf-8
# Copyright 2022 The Chirp Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration file for SHOT SFDA method."""
from chirp import config_utils
from chirp.projects.sfda import model_utils
from ml_collections import config_dict


def get_image_config() -> config_dict.ConfigDict:  # pylint: disable=missing-function-docstring

  # Configure adaptation
  image_config = config_dict.ConfigDict()

  optimizer_cfg = config_dict.ConfigDict()
  optimizer_cfg.optimizer = "adam"
  optimizer_cfg.opt_kwargs = {}
  optimizer_cfg.weight_decay = 0.
  optimizer_cfg.learning_rate = 1e-4
  optimizer_cfg.use_cosine_decay = True
  optimizer_cfg.trainable_params_strategy = model_utils.TrainableParams.BN
  image_config.optimizer_config = optimizer_cfg

  # Method-specifc hparam
  image_config.beta = 0.3

  # Forward options
  image_config.num_epochs = 10
  image_config.use_dropout = False
  image_config.update_bn_statistics = True
  return image_config


def get_audio_config() -> config_dict.ConfigDict:  # pylint: disable=missing-function-docstring

  # Configure adaptation
  audio_config = config_dict.ConfigDict()

  optimizer_cfg = config_dict.ConfigDict()
  optimizer_cfg.optimizer = "adam"
  optimizer_cfg.opt_kwargs = {}
  optimizer_cfg.weight_decay = 0.
  optimizer_cfg.learning_rate = 1e-5
  optimizer_cfg.use_cosine_decay = True
  optimizer_cfg.trainable_params_strategy = model_utils.TrainableParams.BN
  audio_config.optimizer_config = optimizer_cfg

  # Method-specifc hparam
  audio_config.beta = 0.

  # Forward options
  audio_config.num_epochs = 10
  audio_config.use_dropout = False
  audio_config.update_bn_statistics = False
  return audio_config


def get_config() -> config_dict.ConfigDict:

  method_config = config_dict.ConfigDict()
  method_config.sfda_method = config_utils.callable_config("shot.SHOT")
  method_config.audio = get_audio_config()
  method_config.image = get_image_config()
  return method_config
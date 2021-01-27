## Configuring your session on M2

Your session's settings should look like the following image: 

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/data_team_fields.png?raw=true)

__Additional environments to load__: `environment`

__Custom module paths__: `module use $HOME/text_mining_with_python`

__Memory__: 
Below are the memory requirements to read in each data set. You may want to increase your memory (maybe from `6G` to `10G`, for example) if you expect to create many variables while processing your data. 
- Project Gutenberg: start with `6G`. Increase memory if you make a large corpus.
- EDGAR: start with `6G`. Increase memory if you add many more companies. 
- Hansard: `64G`
- US Congress: `6G`
- Dallas City Council: `6G`
- Houston City Council: `6G`
- Reddit: 
  - the Reddit data is broken into 92 (yes, 92!) files totalling ~`250G` of Reddit data!!! You can access individual files using ~`6-15G`, but please see Steph if you need help.

## Source Information

The Notebook, "Instructions for Accessing Data" (hist3368-week4-access-data.ipynb), was written by Steph Buongiorno, project manager to Dr. Jo Guldi and PhD student in Applied Science in Engineering at Southern Methodist University. Additional code for reading in data was provided by Alexander Cerpa, computer science undergraduate at Southern Methodist Univeristy. A version one of this notebook was written by [Dr. Eric Godat](https://github.com/egodat), member of OIT at Southern Methodist University. Version one can be found on Southern Methodist University's GitHub at: [SouthernMethodistUniversity/text_mining_data_sets/DataAccess.ipynb](https://github.com/SouthernMethodistUniversity/text_mining_data_sets/blob/master/DataAccess.ipynb).

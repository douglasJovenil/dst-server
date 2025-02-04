-- Use this file to enable and configure your mods. The mod will only be available in the game
-- if you set "enabled=true"!!!
--
-- Also, during the container startup this file will be copied to both Master/ and Caves/ folders. What's setup here
-- will be available in both shards!
--
-- See the example below:

return {
  ['workshop-1207269058'] = { enabled=true },
  ['workshop-374550642'] =  { configuration_options={ MAXSTACKSIZE=99 }, enabled=true },
  ['workshop-378160973'] =  {
    configuration_options={
      ENABLEPINGS=true,
      FIREOPTIONS=2,
      OVERRIDEMODE=false,
      SHAREMINIMAPPROGRESS=true,
      SHOWFIREICONS=true,
      SHOWPLAYERICONS=true,
      SHOWPLAYERSOPTIONS=2 
    },
    enabled=true 
  },
  ['workshop-501385076'] =  { configuration_options={ quick_harvest=true }, enabled=true },
  ['workshop-661253977'] =  { enabled=true },
  ['workshop-1862534310'] = { enabled=true },
}

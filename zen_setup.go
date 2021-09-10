{{$mid :=819045275896512543}}
{{$r :=sdict "super_hound" 786331185860313129 "super_wiz" 786331078893502524 "super_witch" 784413270038806528 "super_inferno" 784413217883160587 "super_wallbreaker" 784413106717065248 "super_goblin" 784412925707812886 "super_valk" 784412745364799488 "super_giant" 784413054518951956 "Super_minion" 784411939672555580 "super_barbs" 784412013547225109 "super_archer" 784412057458049036}}
{{if eq .Message.ID $mid}}
  {{removeRoleID ($r.Get .Reaction.Emoji.Name) 259200}}
{{end}}

{{$mid :=848212354571042866}}
{{$r :=sdict "supersneakygoblin" 740141274002358322 "superminion" 776200392912273438 "superwizard" 787087524568891422 "superinfernodrag" 776200781723861035 "superwb" 740141524615954443 "superarcher" 776200685288161340 "supergiant" 776200509949607936 "superbarb" 776200650580951071 "superwitch" 776200200149794837 "supericehound" 787087855230255156 "supervalk" 776200373320286229}}
{{if eq .Message.ID $mid}}
  {{removeRoleID ($r.Get .Reaction.Emoji.Name) 60}}
{{end}}
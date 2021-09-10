{/*{{$clan_roles := cslice 355699265609400330 384436509568401408 693625860787273778}}
{{$app_roles := cslice 821922696379760670 821922709562064896 821922710527541258}}
*/} //reference

{{if eq .Reaction.Emoji.Name ":huzzah:"}}  //zen
    {{if .ReactionAdded}}
        {{if hasRoleID 821922696379760670}}
            {{addRoleID 355699265609400330}}
            {{removeRoleID 821922696379760670}}
        {{end}}
    {{end}}
{{end}}
{{else if eq .Reaction.Emoji.Name ":huzzah:"}}  //zenith
    {{if .ReactionAdded}}
        {{if hasRoleID 821922709562064896}}
            {{addRoleID 384436509568401408}}
            {{removeRoleID 821922709562064896}}
        {{end}}
    {{end}}
{{end}}
{{else if eq .Reaction.Emoji.Name ":huzzah:"}}  //academy
    {{if .ReactionAdded}}
        {{if hasRoleID 821922710527541258}}
            {{addRoleID 693625860787273778}}
            {{removeRoleID 821922710527541258}}
        {{end}}
    {{end}}
{{end}}


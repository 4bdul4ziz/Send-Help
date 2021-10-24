{{with .CmdArgs}}
  {{$role := index . 0 | reFind `/([FfRrEe]){\d{17,19}\w+/g` | toInt64 | $.Guild.GetRole}}
  {{if $role}}

    {{with $.Message.Mentions}}
      {{range .}}{{ giveRoleID .ID $role.ID}}{{end}}
<:huzzah:834839960515379200> Added {{$role.Name}}
to {{.}} 
    {{else}}
No User Mentioned.
    {{end}}

  {{else}}
Role does not exist.
  {{end}}

{{else}}
Syntax: `-mra <Role:ID/Mention> <User:Mention>` 
{{end}}
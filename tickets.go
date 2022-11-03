{{ $val := createTicket nil .User.Username }}
{{ $args := parseArgs 1 "" (carg "user" "target user") }}
{{$userid := ($args.Get 0) }}

{{$zenMID :=827433436138307627}}
{{$zenithMID :=827433553636884501}}
{{$zenacMID :=827433746655215678}}
{{$dojoMID :=898006006477492244}}
{{$friendMID := 827433254340263966}}
{{ $user := .User }}
{{ $avatar := ("https://cdn.discordapp.com/attachments/356051234513354753/825483935869960202/Zenred-pfp.png") }}

{{ $embed := complexMessage "content" .User.Mention "embed" (cembed "title" (joinStr "" "A new Friend of Zen has arrived, " .User.Username ", GG!")
"description" "Here is a quick guide of the channels- \n > [#zen-social](https://discord.com/channels/355698225031806978/379988284769828864) - General Chat - You are here \n > [#meet-the-members](https://discord.com/channels/355698225031806978/799731522835185696) - Introduce yourself here \n > [#rcs-news-and-events](https://discord.com/channels/355698225031806978/749110784692453417) - News & Events from RCS \n > [#bot-home-base](https://discord.com/channels/355698225031806978/803287483357462548) - Bot Spam & Music \n > [#apply-to-clan](https://discord.com/channels/355698225031806978/808173961946857493) - To join one of our family's clans!" "color" 15599624 "thumbnail" (sdict "url" $avatar))}}

{{$addroleids := cslice 385045213510369284}}
{{$takeroleids := cslice 827012894087577642 845792096908738560}}

{{if eq .Reaction.MessageID $friendMID}}
    {{if eq .Reaction.Emoji.ID 797949798686261250}}
         {{ range $addroleids }}
         {{- giveRoleID $user . -}}
         {{- end }}
         {{ range $takeroleids }}
        {{- takeRoleID $user . -}}
        {{- end }} 
    {{sendMessage 384804110291173388 $embed}}
    {{end}}
{{end}}


{{if eq .Reaction.MessageID $zenacMID}}
	{{if eq .Reaction.Emoji.ID 710608766906663032 }}
        {{addRoleID 821922710527541258}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 693625399757897789) ": " .User.Mention " is applying to Zen Academy with a Townhall 7")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608811504959549 }}
        {{addRoleID 821922710527541258}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 693625399757897789) ": " .User.Mention " is applying to Zen Academy with a Townhall 8")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608822049439768 }}
        {{addRoleID 821922710527541258}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 693625399757897789) ": " .User.Mention " is applying to Zen Academy with a Townhall 9")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenithMID}}
	{{if eq .Reaction.Emoji.ID 710608835479339058 }}
        {{addRoleID 821922709562064896}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 384438571332927489) ": " .User.Mention " is applying to Zenith with a Townhall 10")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenithMID}}
	{{if eq .Reaction.Emoji.ID 710608844513869865 }}
        {{addRoleID 821922709562064896}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 384438571332927489) ": " .User.Mention " is applying to Zenith with a Townhall 11")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenithMID}}
    {{if eq .Reaction.Emoji.ID 710608855163338802 }}
        {{addRoleID 821922696379760670}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 384438571332927489) ": " .User.Mention " is applying to Zenith with a Townhall 12")}}
        {{createTicket nil .User.Username}}
    {{end}}
{{end}}


{{if eq .Reaction.MessageID $zenMID}}
    {{if eq .Reaction.Emoji.ID 710608868480253992 }}
        {{addRoleID 821922696379760670}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 355698834422235136) ": " .User.Mention " is applying to Zen with a Townhall 13")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenMID}}
    {{if eq .Reaction.Emoji.ID 829071576275877988 }}
        {{addRoleID 821922696379760670}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 355698834422235136) ": " .User.Mention " is applying to Zen with a Townhall 14")}}
    {{end}}
{{end}}


{{if eq .Reaction.MessageID $dojoMID}}
    {{if eq .Reaction.Emoji.ID 898012184678895640 }}
        {{addRoleID 898007278983204874}}
        {{removeRoleID 827012894087577642}}
        {{removeRoleID 845792096908738560}}
        {{ sendMessageNoEscape 827342537764110356 (print (mentionRoleID 897683918608814181) ": " .User.Mention " is applying to Zen Dojo")}}
    {{end}}
{{end}}
loop

dreadsensor s
getinfo p
if($s==1)
	send $p 13
	delay 300
end

read v
set a 0
set b A
conc a  $v $b

if($a!=A)
	send $v 13
	delay 300
end
delay 100

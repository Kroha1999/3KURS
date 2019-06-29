loop

dreadsensor s
getinfo p
if($s==1)
	send $p 3
	delay 300
end

read v
set a 0
set b A
conc a  $v $b

if($a!=A)
	send $v 3
	delay 300
end
delay 100

set nid 0
loop

if($nid == 0)
	wait
	read v
	set nid $v
	atget id x
	send $x * $nid
	delay 3000
end


dreadsensor s
getinfo p
if($s==1)
	send $p $nid
	delay 300
end

read v
set a 0
set b A
conc a  $v $b

if($a!=A)
	send $v $nid
	delay 300
end
delay 100

set nid null
loop

if($nid == null)
	wait
	read v
	set nid $v
	atget id x
	send $x * $nid
end


dreadsensor s
if($s==1)
	getinfo p
	send $p $nid
	cbuffer
	delay 300
end

read v
set a 0
set b A
conc a  $v $b

if($a!=A)
	if($v!=0)
		send $v $nid
		delay 300
	end
end
delay 100

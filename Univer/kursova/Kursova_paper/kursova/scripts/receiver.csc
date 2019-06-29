set iden null
loop

if($iden == null)
	atget id x
	send $x
	set iden 1
	delay 300
end


wait
read v
mark $v

rdata $v id x y


cprint ID: $id X: $x Y: $y


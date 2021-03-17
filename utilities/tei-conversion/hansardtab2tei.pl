#! /usr/bin/perl
#
#FileID	SectionID	SentenceID	Speech_ID	Date	Debate	Category	
#Text	Speaker	Constituency	House	Image	Column	Errata	Ententies	Labels
open(HH, "TEIheader.txt") or die;
while ($lin = <HH>) {
	$teiheader .= $lin;
}
close (HH);
open (IN, "hansard_c19_04152021.tsv");
$lin = <IN>;
chop ($lin);
@labels = split("\t", $lin);
$reclen = $#labels;
print $reclen. "\n";
$lim = 1000000;
while ($lin = <IN>){
	chop ($lin);
	@vals = split("\t", $lin);
	for $i (0..$reclen){
		# print $labels[$i] . "=" .  $vals[$i] . "\n";
		$inline{$labels[$i]} = $vals[$i];
		}
	if ($thisfileid ne $inline{"FileID"}) {
		if ($buffer) {
			$buffer .= "</sp>\n</div>\n</text>\n</TEI.2>\n";
			print OUTFILE $buffer;
			$buffer = ""; 
			close (OUTFILE);
			$thisdebate = ""; $thisspeaker = ""; $inadebate = 0;
			}
		$thisdate = $inline{"Date"};
		$filename = "output_3_15-21/" . $thisdate . "." .$inline{"FileID"} . ".xml";
		$thisfileid = $inline{"FileID"};
		print "OPEN NEW FILE " . $filename . "\n";
		($year,$month,$day) = split("-", $thisdate);
		$thisheader = $teiheader;
		$thisheader =~ s/==YEAR==/$year/g;
		$thisheader =~ s/==IDENTIFIER==/$thisfileid/g;
		$buffer = $thisheader;	
		$thisdebate = ""; $thisspeaker = ""; $inadebate = 0;
		open (OUTFILE, ">$filename") or die;
		}
	if ($thisdebate ne $inline{"Debate"}) {
		if ($inadebate) {
			$buffer .= "</sp>\n";
			$buffer .= "</div>\n";
			$thisspeaker = "";
			}	
		$thisdebate = $inline{"Debate"};
		$buffer .= "<div id=\"" . $inline{"SectionID"}. "\"";
		$buffer .= " date=\"" . $inline{"Date"} . "\">\n";
		$tbate = $inline{"Debate"};
		$tbate =~ s/\[//;
		$tbate =~ s/\]//;
		if (!$tbate) {
			$tbate = "MISSING VALUE";
			}
		$buffer .= "<head>" . $tbate . "</head>\n";
		$inadebate = 1;
		}
	if ($thisspeaker ne $inline{"Speaker"}) {
		if ($thisspeaker) {
			$buffer .= "</sp>\n";
			}
		$buffer .= "<sp who=\"" . $inline{"Speaker"} . "\" id=\"";
	  	$buffer .= $inline{"Speech_ID"} . "\">\n";
		$buffer .= "<speaker>" . $inline{"Speaker"} . "</speaker>\n";
		$thisspeaker = $inline{"Speaker"};
		}
	$buffer .= "<s id=\"" . $inline{"SentenceID"} . "\">";
	$thistext = $inline{"Text"};
	$thistext =~ s/\&/\&amp;/g;
	$buffer .= $thistext . "</s>\n";

	$count++;
	}
if ($buffer) {
    $buffer .= "</sp>\n</div>\n</text>\n";
    print OUTFILE $buffer;
    $buffer = "";
    close (OUTFILE);
}




<?php

error_reporting(E_ALL);
ini_set("display_errors", 1);

class Strip {
	private $x = 0.05;
	private $y = 0.05;
	private $z = 0.05;

	public $numberLEDs = 64;
	public $startX = 0;
	public $startY = 0;
	public $angle = 0;

	function generatePoints() {
		$points = array();

		for ($i = 0; $i < 64; $i++) {
			if ($i >= $this->numberLEDs) {
				$points[] = array("point" => array(-5,-5,-5));
				continue;
			}

			if ($this->angle == 0) {
				$points[] = array("point" => array(-4.8 + ($i + $this->startX) * $this->x, 0.0, -1.0 + $this->startY * $this->y));
			} else {
				$points[] = array("point" => array(-4.8 + $this->startX * $this->x, $this->z, -1.0 + ($i + $this->startY) * $this->y));
			}
		}

		return $points;
	}
}

$strip0 = new Strip();
$strip0->numberLEDs = 64;
$strip0->startX = 0;
$strip0->startY = 22;
$strip0->angle = 0;

$strip1 = new Strip();
$strip1->numberLEDs = 29;
$strip1->startX = 35;
$strip1->startY = 23;
$strip1->angle = 90;

$strip2 = new Strip();
$strip2->numberLEDs = 64;
$strip2->startX = 36;
$strip2->startY = 38;
$strip2->angle = 0;

$strip3 = new Strip();
$strip3->numberLEDs = 29;
$strip3->startX = 50;
$strip3->startY = 9;
$strip3->angle = 90;

$strip4 = new Strip();
$strip4->numberLEDs = 64;
$strip4->startX = 50;
$strip4->startY = 8;
$strip4->angle = 0;

$strip5 = new Strip();
$strip5->numberLEDs = 22;
$strip5->startX = 87;
$strip5->startY = 26;
$strip5->angle = 90;

$strip6 = new Strip();
$strip6->numberLEDs = 43;
$strip6->startX = 87;
$strip6->startY = 25;
$strip6->angle = 0;

$strip7 = new Strip();
$strip7->numberLEDs = 29;
$strip7->startX = 99;
$strip7->startY = 9;
$strip7->angle = 90;

$strip8 = new Strip();
$strip8->numberLEDs = 41;
$strip8->startX = 114;
$strip8->startY = 0;
$strip8->angle = 90;

$strip9 = new Strip();
$strip9->numberLEDs = 43;
$strip9->startX = 115;
$strip9->startY = 0;
$strip9->angle = 0;

$strip10 = new Strip();
$strip10->numberLEDs = 64;
$strip10->startX = 115;
$strip10->startY = 18;
$strip10->angle = 0;

$strip11 = new Strip();
$strip11->numberLEDs = 43;
$strip11->startX = 115;
$strip11->startY = 40;
$strip11->angle = 0;

$points = array();

$points = array_merge($points, $strip0->generatePoints());
$points = array_merge($points, $strip1->generatePoints());
$points = array_merge($points, $strip2->generatePoints());
$points = array_merge($points, $strip3->generatePoints());
$points = array_merge($points, $strip4->generatePoints());
$points = array_merge($points, $strip5->generatePoints());
$points = array_merge($points, $strip6->generatePoints());
$points = array_merge($points, $strip7->generatePoints());
$points = array_merge($points, $strip8->generatePoints());
$points = array_merge($points, $strip9->generatePoints());
$points = array_merge($points, $strip10->generatePoints());
$points = array_merge($points, $strip11->generatePoints());

if (file_put_contents('entrance.json', json_encode($points))) {
	echo 'Layout generated with ' . count($points) . ' points.';
} else {
	echo 'Error: Can\'t generate the layout file';
}

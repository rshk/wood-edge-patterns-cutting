module pattern_cut(m, pattern) {
  // We want to cut the mth module out..
  n = pattern[0];
  e = pattern[1];
  s = pattern[2];
  w = pattern[3];

  sh = 3; // Slice height
  so = m * sh; // Slice offset

  if (n=="H") { translate([-5,0,so]) cube([10, 4, sh]); }
  else if (n=="T") { translate([-5,1,so]) cube([10, 3, sh]); }

  if (e=="H") { translate([0,-5,so]) cube([4, 10, sh]); }
  else if (e=="T") { translate([1,-5,so]) cube([3, 10, sh]); }

  if (s=="H") { translate([-5,-4,so]) cube([10, 4, sh]); }
  else if (s=="T") { translate([-5,-4,so]) cube([10, 3, sh]); }

  if (w=="H") { translate([-4,-5,so]) cube([4, 10, sh]); }
  else if (w=="T") { translate([-4,-5,so]) cube([3, 10, sh]); }
}

elems = [
"H---",
"-H--",
"--H-",
"---H",
"T--T",
"TT--",
"-TT-",
"--TT",
"-T-T",
"T-T-",
"-H--",
"-HH-",
"--H-",
];


difference() {
  translate([0, 0, 30]) cube([6, 6, 60], center=true);

  for (i = [0:len(elems)]) {
    pattern_cut(i, elems[i]);
  }
}

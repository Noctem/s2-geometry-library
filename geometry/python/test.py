#!/usr/bin/env python
# Copyright 2006 Google Inc. All Rights Reserved.

import unittest
from s2 import *

class S2TestCase(unittest.TestCase):

  def testContainsIsWrappedCorrectly(self):
    london = S2LatLngRect(S2LatLng.FromDegrees(51.3368602, 0.4931979),
                          S2LatLng.FromDegrees(51.7323965, 0.1495211))
    e14lj = S2LatLngRect(S2LatLng.FromDegrees(51.5213527, -0.0476026),
                         S2LatLng.FromDegrees(51.5213527, -0.0476026))
    self.assertTrue(london.Contains(e14lj))

  def testS2CellIdEqualsIsWrappedCorrectly(self):
    london = S2LatLng.FromDegrees(51.5001525, -0.1262355)
    cell = S2CellId.FromLatLng(london)
    same_cell = S2CellId.FromLatLng(london)
    self.assertEqual(cell, same_cell)

  def testS2CellIdComparsionIsWrappedCorrectly(self):
    london = S2LatLng.FromDegrees(51.5001525, -0.1262355)
    cell = S2CellId.FromLatLng(london)
    self.assertTrue(cell < cell.next())
    self.assertTrue(cell.next() > cell)

  def testS2HashingIsWrappedCorrectly(self):
    london = S2LatLng.FromDegrees(51.5001525, -0.1262355)
    cell = S2CellId.FromLatLng(london)
    same_cell = S2CellId.FromLatLng(london)
    # FIXME: Hash function is commented out in the SWIG, and broken.
    #self.assertEquals(hash(cell), hash(same_cell))

  def testCovererIsWrapperCorrectly(self):
    london = S2LatLngRect(S2LatLng.FromDegrees(51.3368602, 0.4931979),
                          S2LatLng.FromDegrees(51.7323965, 0.1495211))
    e14lj = S2LatLngRect(S2LatLng.FromDegrees(51.5213527, -0.0476026),
                         S2LatLng.FromDegrees(51.5213527, -0.0476026))
    coverer = S2RegionCoverer()
    covering = coverer.GetCovering(e14lj)
    for cellid in covering:
      self.assertTrue(london.Contains(S2Cell(cellid)))


if __name__ == "__main__":
  unittest.main()

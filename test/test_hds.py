from unittest import TestCase
import numpy as np

import starlink.hds as hds


# Dictionary of things to write into a test HDS file.  The key is the
# name, and then the values are the type, the dimensions and the
# values.
char_array = [' Begin FrameSet                 ',
              ' Nframe = 5                     ',
              ' Currnt = 5                     ',
              ' Lnk2 = 1                       ',
              ' Lnk3 = 1                       ']

attributes_to_write = {
    'ONEDCHAR': ('_CHAR*1', None, 't'),
    'BOOLEAN': ('_LOGICAL', None, True),
    'DOUBLE': ('_DOUBLE', None, 3e-8),
    'REAL': ('_REAL', None, 3.76),
    'INTEGER': ('_INTEGER', None, 42),
    'BYTE': ('_BYTE', None, np.byte(2)),
    'UBYTE': ('_UBYTE', None, np.ubyte(3)),
    'DOUBLE_ARRAY': ('_DOUBLE', [3,2], [[-1.0, np.nan],[1.2, 2.3],[3.4, 4.5]]),
    'CHARARRAY':('_CHAR*32',[5], char_array),
    'INT_ARRAY': ('_INTEGER', [10,20], np.arange(10*20).reshape((10,20))),
    'BOOL_ARRAY': ('_LOGICAL', [1,2,3], [[[ True, False,  True],[False,  True, False]]])
}

keys = list(attributes_to_write.keys())
keys.sort()



class TestHds(TestCase):

    def test_create_ndf(self):
        loc = hds.new('test.sdf', 'HDS_TEST', 'HDSEXAMPLE')

        # Write each attribute as a new component in the NDF.
        for attribute in keys:

            type_, dims, value = attributes_to_write[attribute]

            # Create the locator for the new component
            if dims:
                comploc = loc.new(attribute,  type_, dims)
            else:
                comploc = loc.new(attribute, type_)


            comploc.put(value)

            # Annul the locator.
            comploc.annul()
        loc.annul()


        # Now open the written NDF and read each component.
        loc = hds.open('test.sdf', 'READ')
        for i in range(loc.ncomp):
            comploc = loc.index(i)
            name = comploc.name

            exp_type, exp_dims, exp_value = attributes_to_write[name]

            self.assertEqual(comploc.type, exp_type)
            if exp_dims:
                self.assertSequenceEqual(comploc.shape.tolist(), np.asarray(exp_dims).tolist())

            value = comploc.get()

            if comploc.type.startswith('_CHAR'):
                if exp_dims:
                    flatvalue = [i.decode('ascii') for i in value.flatten()]
                    value = np.asarray(flatvalue).reshape(value.shape)
                else:
                    value = value.decode('ascii')

            if comploc.type in ['_DOUBLE', '_REAL']:
                np.testing.assert_allclose(value,exp_value, verbose=True)
            else:

                np.testing.assert_equal(value, exp_value)


if __name__ == "__main__":
    unittest.main()
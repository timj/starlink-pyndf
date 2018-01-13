#if !defined( HDS_TYPES_INCLUDED ) /* hds_types.h already included? */
#define HDS_TYPES_INCLUDED 1
/*
*+
*  Name:
*     hds_types.h

*  Type of Module:
*     C include file.

*  Purpose:
*     Define public HDS-specific data types.

*  Description:
*     This file defines the public types that are used in the HDS
*     public API.

*  Authors:
*     TIMJ: Tim Jenness (JAC, Hawaii)
*     ./make-hds-types program

*  History:
*     21-Oct-2005 (TIMJ):
*        Original version of C program (via auto-generation).
*     12-Jan-2018 (./make-hds-types):
*        Generated
*     No further changes -- do not edit this file

*-
*/

#include <stddef.h>

#include <inttypes.h>

/* Public type for dealing with HDS locators */
/* The contents of the struct are private to HDS. The only public */
/* part is the HDSLoc typedef. Never use 'struct LOC' directly.   */
typedef struct LOC HDSLoc;

/* Public type for specifying HDS dimensions */
typedef int hdsdim;
#define HDS_DIM_FORMAT "d"

/* Public type for Logical type */
typedef int hdsbool_t;
#define HDS_BOOL_FORMAT "d"

#endif /* _INCLUDED */


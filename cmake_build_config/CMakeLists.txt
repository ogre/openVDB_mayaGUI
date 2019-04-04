
#cmake --Wno-dev -G "Visual Studio 15 2017 Win64" ..\openVDB_mayaGUI\cmake_build_config\

cmake_minimum_required( VERSION 3.12 )
#set(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS true)

if(POLICY  CMP0074)
  cmake_policy(SET  CMP0074 NEW)
endif()

project (openvdb_MayaGUI)

set (CMAKE_CXX_STANDARD 11)

set ( CMAKE_BUILD_TYPE "Release" )




find_package( OpenGL REQUIRED )
message( "OPENGL_LIBRARIES " ${OPENGL_LIBRARIES} )


set ( ZLIB_ROOT $ENV{ZLIB_ROOT} )
find_package( ZLIB REQUIRED )

set ( Blosc_DIR "./CMake" )
find_package( Blosc REQUIRED )


set ( BOOST_ROOT $ENV{BOOST_ROOT} )
set(Boost_USE_STATIC_LIBS ON)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME Off)
ADD_DEFINITIONS(-DBOOST_ALL_NO_LIB)
#SET ( Boost_NO_BOOST_CMAKE ON )
#SET ( Boost_NO_SYSTEM_PATHS ON )
find_package(Boost REQUIRED COMPONENTS filesystem)
include_directories ( ${Boost_INCLUDE_DIR} )
message ( "Boost_INCLUDE_DIR: " ${Boost_INCLUDE_DIR} )


set ( MAYA_ROOT $ENV{MAYA_ROOT} )
file(TO_NATIVE_PATH ${MAYA_ROOT} MAYA_ROOT)
LIST(APPEND CMAKE_MODULE_PATH  "${MAYA_ROOT}CMake" )
find_package( Maya REQUIRED )
set ( Maya_INCLUDE_DIR "/${Maya_INCLUDE_DIR}" )
include_directories ( "/"${Maya_INCLUDE_DIR} )
message ( "Maya_INCLUDE_DIR: " ${Maya_INCLUDE_DIR} )
message ( "Maya_LIBRARIES: " ${Maya_LIBRARIES} )
add_definitions( -DREQUIRE_IOSTREAM )


set ( OPENEXR_ROOT $ENV{OPENEXR_ROOT} )
file(TO_NATIVE_PATH ${OPENEXR_ROOT} OPENEXR_ROOT)
LIST(APPEND CMAKE_MODULE_PATH  "$ENV{OPENEXR_ROOT}CMake" )
find_package( OpenEXR REQUIRED )
include_directories ( ${OPENEXR_INCLUDE_DIRS} )


set ( TBB_DIR "./CMake" )
FIND_PACKAGE ( TBB REQUIRED )

add_definitions( -DOPENVDB_STATICLIB  )
add_definitions( -DOPENVDB_OPENEXR_STATICLIB )
add_definitions( -DOPENVDB_3_ABI_COMPATIBLE )
set ( OPENVDB_ROOT $ENV{OPENVDB_ROOT} )
file( TO_NATIVE_PATH ${OPENVDB_ROOT} OPENVDB_ROOT )
LIST(APPEND CMAKE_MODULE_PATH  "$ENV{OPENVDB_ROOT}CMake" )
find_package( OPENVDB REQUIRED )
include_directories ( ${OPENVDB_INCLUDE_DIRS} )
include_directories ( '../openVDB_mayaGUI' )


FILE( GLOB openvdb_MayaGUI_SRC
	"../openVDB_mayaGUI/*.h"
	"../openVDB_mayaGUI/*.cpp"
	)


ADD_LIBRARY(openvdb_MayaGUI SHARED ${openvdb_MayaGUI_SRC} )

set ( ADDITIONAL_LINK_FLAGS " ")
if (WIN32)
	#add_definitions( -DOPENVDB_DLL )
	add_definitions( -D_BOOL )
	add_definitions( -DNT_PLUGIN )
	add_definitions( -DWIN32_LEAN_AND_MEAN )
	add_definitions( -DNOMINMAX )
	add_definitions( -D_USE_MATH_DEFINES )

	add_definitions( -DOPENVDB_STATICLIB  )
	add_definitions( -DOPENVDB_OPENEXR_STATICLIB )
	add_definitions( -DOPENVDB_3_ABI_COMPATIBLE )

	set ( ADDITIONAL_LINK_FLAGS
		"${ADDITIONAL_LINK_FLAGS} /export:initializePlugin /export:uninitializePlugin" )
	set_target_properties( openvdb_MayaGUI PROPERTIES SUFFIX ".mll" )

	#set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} /MT")
	#set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} /MT")
ELSE()
	add_definitions( -D_BOOL )
	add_definitions( -DLINUX )
	add_definitions( -fPIC )
	add_definitions( -fno-strict-aliasing )
	add_definitions( -ftemplate-depth-100 )
	add_definitions( -DOPENVDB_3_ABI_COMPATIBLE )
endif (WIN32)


set_target_properties( openvdb_MayaGUI PROPERTIES PREFIX "")
set_target_properties( openvdb_MayaGUI PROPERTIES LINK_FLAGS ${ADDITIONAL_LINK_FLAGS} )


message ( "linking to Maya_LIBRARIES: " 	${Maya_LIBRARIES} )
message ( "linking to OPENEXR_LIB_Half: " 	${OPENEXR_LIB_Half} )
message ( "linking to OPENVDB_LIBRARIES: " 	${OPENVDB_LIBRARIES} )
message ( "linking to Boost_LIBRARIES: " 	${Boost_LIBRARIES} )
message ( "linking to BLOSC_blosc_LIBRARY: " 	${BLOSC_blosc_LIBRARY} )
message ( "linking to Tbb_TBB_LIBRARY: " 	${Tbb_TBB_LIBRARY} )
message ( "linking to ZLIB_LIBRARY: " 	${ZLIB_LIBRARY} )

TARGET_LINK_LIBRARIES( openvdb_MayaGUI
						${Boost_LIBRARIES}
						${Maya_LIBRARIES}
						${OPENEXR_LIB_Half}
						${OPENVDB_LIBRARIES}
						${BLOSC_blosc_LIBRARY}
						${DELIGHT_LIBRARY}
						${OPENGL_LIBRARIES}
						${ZLIB_LIBRARY}
						${Tbb_TBB_LIBRARY}
						${SEEXPR_LIBRARY}
					)



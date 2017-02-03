Find_Package(SWIG REQUIRED)
Find_Package(PythonInterp REQUIRED)
Find_Package(PythonLibs REQUIRED)

include(UseSWIG)

include_directories(${PYTHON_INCLUDE_PATH})

set_source_files_properties(s2.i PROPERTIES CPLUSPLUS ON)
swig_add_module(s2 python s2.i)
swig_link_libraries(s2 s2 s2cellid s2util ${PYTHON_LIBRARIES})

set(PYTHON_SITE_PACKAGES "${CMAKE_INSTALL_LIBDIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages")

install(
	TARGETS _s2
	DESTINATION "${PYTHON_SITE_PACKAGES}/s2"
)
install(
	FILES __init__.py ${CMAKE_CURRENT_BINARY_DIR}/s2.py
	DESTINATION "${PYTHON_SITE_PACKAGES}/s2"
)

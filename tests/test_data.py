import sys
sys.path.insert(0, '.')
from dashboard.dashboard_dash import D


def test_data_loads():
    d = D()
    assert d['la'].shape[0] > 0, "LATAM migration data is empty"
    assert d['lg'].shape[0] >= 0, "LATAM→Germany data failed to load"
    assert d['gt'].shape[0] > 0, "German university trend data is empty"
    assert d['ff'].shape[0] > 0, "Field of study data is empty"


def test_profiles_data():
    d = D()
    la = d['la']
    assert 'field_of_study' in la.columns, "field_of_study column missing"
    assert 'enrollment_reason' in la.columns, "enrollment_reason column missing"
    assert 'language_proficiency_test' in la.columns, \
        "language_proficiency_test column missing"
    fos = la['field_of_study'].dropna().value_counts()
    assert len(fos) > 0, "field_of_study value_counts() returned empty"


def test_charts_have_data():
    d = D()
    fos = d['la']['field_of_study'].dropna().value_counts()
    assert len(fos) >= 3, \
        f"Expected at least 3 field_of_study categories, got {len(fos)}"


if __name__ == '__main__':
    test_data_loads()
    test_profiles_data()
    test_charts_have_data()
    print("All tests passed.")

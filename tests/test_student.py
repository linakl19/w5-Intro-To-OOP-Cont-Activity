from school_schedule.student import Student

def test_correct_atributes_when_instantiating_class():
    # Arrange
    name = "Natalia"
    grade = "Senior"
    classes_list = ["math", "art"]

    # Act
    student = Student(name, grade, classes_list)

    # Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes_list

def test_default_class_attribute_class_empty_list():
    # Arrange
    name = "Lina"
    grade = "Senior"
    classes_list = []

    # Act
    student = Student(name, grade)

    # Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes_list

def test_add_class_increses_classes_attribute_length():
    # Arrange
    name = "Natalia"
    grade = "Senior"
    classes_list = ["Math", "Art"]
    student = Student(name, grade, classes_list)

    # Act
    updated_classes_list = student.add_class("CS")

    # Assert
    assert student.classes == updated_classes_list


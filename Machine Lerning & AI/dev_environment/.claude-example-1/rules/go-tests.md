---
paths:
  - "**/*_test.go"
  - "pkg/mock/**"
---

# Go Test Rules

These rules apply only when working with Go test files ending in `_test.go`.

## General testing style

- Always use external test packages: `package foo_test` (not `package foo`). This avoids import cycles and ensures tests consume the package like an external caller.
- Write tests using `github.com/stretchr/testify`.
- Prefer table-driven tests when testing multiple cases.
- Keep test case names clear and human-readable.
- Use `t.Run(name, func(t *testing.T) { ... })` for subtests.
- Do not test implementation details unless necessary.
- Test observable behavior, edge cases, and error paths.
- Keep tests short and focused.
- Skip trivial/obvious tests (e.g., simple struct constructors). Every test should validate meaningful behavior.
- Prefer testing higher-level functions that exercise multiple internals over testing each small helper individually.
- Aim for maximum coverage, but every test must validate real behavior — never write a test solely to cover a line.
- Use `TestMain`, setup helpers, and `t.Cleanup` for shared setup/teardown when it reduces duplication.
- Use `t.Parallel()` for tests that don't share mutable state.
- Name tests as `TestFunctionName_Scenario` (e.g., `TestLogin_InvalidPassword`).
- Place test fixture files in a `testdata/` directory (ignored by `go build` by convention).

## Assertions

Always use `github.com/stretchr/testify`:
- `require.NoError(t, err)` when the test cannot continue after an error.
- `assert.Equal(t, expected, actual)` for normal value comparisons.
- `assert.ErrorIs(t, err, target)` when checking wrapped errors.

## Mocking

Use `github.com/stretchr/testify/mock` for mocking dependencies.
- Mock all external dependencies (APIs, services, file I/O, etc.).
- Exception: do not mock the database when testing real DB scenarios.
- Define mock structs embedding `mock.Mock`.
- Use `mock.On("Method", args...).Return(...)` to set expectations.
- Call `mock.AssertExpectations(t)` at the end of each test.
- If a mock is likely reused, place it in `pkg/mock/` under the `mock` package.

## Error testing

- For exact sentinel errors, use `errors.Is`.
- For typed errors, use `errors.As`.
- Avoid comparing error strings unless the string itself is part of the public contract.

## Test structure

Use this structure when reasonable:

```go
func TestThing_ValidInput(t *testing.T) {
	tests := map[string]struct {
		input   string
		want    string
		wantErr bool
	}{
		"valid input": {
			input: "example",
			want:  "expected",
		},
	}

	for name, tt := range tests {
		t.Run(name, func(t *testing.T) {
			// Arrange
			mockSvc := new(mock.ServiceMock)
			mockSvc.On("DoStuff", tt.input).Return(tt.want, nil)

			// Act
			got, err := Thing(tt.input)

			if tt.wantErr {
				require.Error(t, err)
				return
			}

			// Assert
			require.NoError(t, err)
			assert.Equal(t, tt.want, got)
			mockSvc.AssertExpectations(t)
		})
	}
}
```

## Commands

- Run tests: `go test ./...`
- Run with coverage: `go test -cover ./...`
- Run with verbose output: `go test -v ./...`
- Run specific test: `go test -run TestThing ./...`
- Run with race detector: `go test -race ./...`
- Run with coverage report: `go test -coverprofile=coverage.out ./... && go tool cover -html=coverage.out`
